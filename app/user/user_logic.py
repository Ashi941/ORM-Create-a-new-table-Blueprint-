from flask_restful import  Resource
from app.user.user_tables import Users
from app import db
from flask import request
class GetUsers(Resource):
    def get(self):
        user = Users.query.all()
        if user:
            return {'username': user.username, 'email':user.email}
        else:
            return {'message':'User not found'},404
       
    # to create users
       
    def post(self):
        try:
            data = request.get_json()
            new_user = Users (
                username=data.get('username'),
                password=data.get('password'),
                email=data.get('email'),
                mobile=data.get('mobile'),
                city=data.get('city'),
                designation=data.get('designation')
 
 
            )
            db.session.add(new_user)
            db.session.commit()
            return {'message':'User registered sucessfully'},201
        except Exception as e:
            print(e)
            return {'message':'User registration failed'},500