from flask import Flask
from flask import request
from flask import Response
from marshmallow import exceptions
import requests


from messages import send_message, process_incoming_message, retrieve_all_messages, process_outgoing_message
from serializers import Message, OutputMessage
from db_connection import session


app = Flask(__name__)
db_session = session()


@app.route("/", methods=['POST'])
def webhook_handler():
    message = request.get_json()
    status = process_incoming_message(message, db_session)
    return Response("ok", status=200)


@app.route("/messages", methods=["POST"])
def send_message_handler():
    body = request.json
    schema = Message()
    try:
        serialized_message = schema.load(body)
    except exceptions.ValidationError:
        return Response("{'message': 'Invalid field in body'}", status=422)

    response = send_message(serialized_message["chat_id"], serialized_message["message"])
    process_outgoing_message(response, db_session)
    return response
    

@app.route("/messages", methods=["GET"])
def retrieve_messages_handler():
    schema = OutputMessage(many=True)
    
    all_messages = retrieve_all_messages()
    serialized_messages = schema.dump(all_messages)
    return serialized_messages



if __name__ == '__main__':
   app.run(debug=True)
