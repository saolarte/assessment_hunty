import sys
import unittest
from unittest.mock import MagicMock, call

from messages import send_message, process_outgoing_message, process_incoming_message

outgoing = {
    "ok": True,
    "result": {
        "chat": {
            "first_name": "Jennifer",
            "id": 1553231911,
            "last_name": "Alarcón",
            "type": "private"
        },
        "date": 1686476335,
        "from": {
            "first_name": "assistant",
            "id": 6091138289,
            "is_bot": True,
            "username": "santiagoassist_bot"
        },
        "message_id": 63,
        "text": "Hola"
    }
}

incoming = {'update_id': 306231227, 'message': {'message_id': 64, 'from': {'id': 1466389253, 'is_bot': False, 'first_name': 'Santiago', 'last_name': 'Olarte', 'language_code': 'es'}, 'chat': {'id': 1466389253, 'first_name': 'Santiago', 'last_name': 'Olarte', 'type': 'private'}, 'date': 1686476547, 'text': 'Hello'}}



class TestProcessOutgoingMessages(unittest.TestCase):
    def test_session_calls(self):
        
        session_mock = MagicMock()
        process_incoming_message(incoming, session_mock)
        self.assertEquals(len(session_mock.method_calls), 3)




if __name__ == '__main__':
    unittest.main()