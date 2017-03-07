from mongoengine import Document, fields

class Student(Document):
    name = fields.StringField()
    grade = fields.IntField()
