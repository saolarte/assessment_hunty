import requests

from db_connection import Message


TOKEN = "6091138289:AAFIn1nRmqaqJ5ZMuSY8mM5n3kUJ-iz41mE"



def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    body = {
                'chat_id': chat_id,
                'text': text
                }
    r = requests.post(url,json=body)
    return r.json()


def process_outgoing_message(message, db_session):
    new_message = Message(
        chat_id=message['result']['chat']['id'],
        id=message['result']['message_id'],
        text=message['result']['text'],
        incoming=False
    )
    db_session.add(new_message)
    db_session.commit()
    db_session.close()
    return True


def process_incoming_message(message, db_session):
    new_message = Message(
        chat_id=message['message']['chat']['id'],
        id=message['message']['message_id'],
        text=message['message']['text'],
        incoming=True
    )
    db_session.add(new_message)
    db_session.commit()
    db_session.close()
    return True
 
def retrieve_all_messages(db_session):
    users = db_session.query(Message).all()
    return users

