from marshmallow import Schema, fields

class OutputMessage(Schema):
    chat_id = fields.Int()
    message = fields.Str(attribute="text")
    incoming = fields.Int()

class Message(Schema): 
    chat_id = fields.Int()
    message = fields.Str()
