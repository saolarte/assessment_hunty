Simple app to send and receive messages using Telegram Bot API

The app is set up to respond using a Telegram bot with the following ID: @santiagoassist_bot

The service consists of the following endpoints:

POST /: Works as webhook for Telegram API. Processes messages that come from Telegram App UI and stores them in the Database

GET /messages: Retrieves from Database all messages that have been sent and received.

POST /messages: Sends a message to Telegram API. Body should look like the following:
{
    "chat_id": 1466389253
    "message": "Hello"
}



How to run the app?
- Install dependencies
    pipenv install
- Start virtual environment
    pipenv shell
- Run the app
    python main.py
