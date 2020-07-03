from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class User(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help='user_id cannot be blank')
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM timetable.user WHERE user_id={data['user_id']};""")
        except:
            return{"message":"there is an error connecting to user table."},500
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help='user_id cannot be blank')
        parser.add_argument('dept_id',type=int,required=True,help='dept_id cannot be blank')
        parser.add_argument('year',type=int,required=True,help='year cannot be blank')
        parser.add_argument('password',type=str,required=True,help='password cannot be blank')
        parser.add_argument('username',type=str,required=True,help='username cannot be blank')
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.user VALUES({data['user_id']},
                                                        {data['dept_id']},
                                                        {data['year']},
                                                        '{data['password']}',
                                                        '{data['username']}')""")
        except:
            return{"message":"There is an error connecting to the usertable"},500
        return {"message":"Sucessfully inserted"},201

class Users():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @classmethod
    def getUsersByUsername(cls,username):
        result=query(f""" SELECT username,password FROM user WHERE username='{username}'""",return_json=False)
        if len(result)>0: return Users(result[0]['username'],result[0]['password'])
        return None
    #@classmethod
    #def getAdminByUsername(cls,username):
     #   result=query(f""" SELECT user_id,username,password FROM user WHERE user_id='{user_id}'""",return_json=False)
      #  if len(result)>0: return Users(result[0]['user_id'],result[0]['username'],result[0]['password'])
       # return None


class Userlogin(Resource):
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help="username cannot be left blank")
        parser.add_argument('password',type=str,required=True,help="password cannot be left blank")
        data=parser.parse_args()
        users=Users.getUsersByUsername(data['username'])
        if users and safe_str_cmp(users.password,data['password']):
            access_token=create_access_token(identity=users.username,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials"},401
