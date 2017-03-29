from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from app.models import db,Users, UsersSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

users = Blueprint('users', __name__)

schema = UsersSchema(strict=True)

api = Api(users)

class CreateListUsers(Resource):
    def get(self):
        users_query = Users.query.all()
        results = schema.dump(users_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            print(raw_dict)
            user = Users(request_dict['firstName'], request_dict['lastName'], request_dict['email'], request_dict['age'], request_dict['birthDate'], request_dict['zipcode'])

            user.add(user)

            query = Users.query.get(user.id)
            results = schema.dump(query).data
            return results, 201

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 403
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 403
            return resp

class GetUpdateDeleteUser(Resource):
    def get(self, id):
        user_query = Users.query.get_or_404(id)
        result = schema.dump(user_query).data
        return result

    def patch(self, id):
        user = Users.query.get_or_404(id)
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            request_dict = raw_dict['data']['attributes']
            for key, value in request_dict.items():
                setattr(user, key, value)

            user.update()
            return self.get(id)

        except ValidationError as err:
            resp = jsonify({"error": err.messages})
            resp.status_code = 401
            return resp

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

    def delete(self, id):
        user = Users.query.get_or_404(id)
        try:
            delete = user.delete(user)
            response = make_response()
            response.status_code = 204
            return response

        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({"error": str(e)})
            resp.status_code = 401
            return resp

api.add_resource(CreateListUsers, '.json')
api.add_resource(GetUpdateDeleteUser, '/<int:id>.json')