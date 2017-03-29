from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    birthDate = db.Column(db.Date)
    zipcode = db.Column(db.Integer, nullable = False)

    def __init__(self, firstName, lastName, email, age, birthDate, zipcode):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.birthDate = birthDate
        self.zipcode = zipcode

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class UsersSchema(Schema):
    not_blank = validate.Length(min=1, error='You cannot leave this field blank')

    id = fields.Integer(dump_only=True)
    firstName = fields.String(validate=not_blank)
    lastName = fields.String(validate=not_blank)
    email = fields.String(validate=not_blank)
    age = fields.Integer(required=True)
    birthDate = fields.String(validate=not_blank)
    zipcode = fields.Integer(required = True)

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/users/"
        else:
            self_link = "/users/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'users'


