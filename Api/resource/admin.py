from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class Admin(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('admin_id',type=str,required=True,help='admin_id cannot be blank')
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM timetable.admin WHERE username={data['admin_id']};""")
        except:
            return{"message":"there is an error connecting to user table."},500
    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help='username cannot be blank')
        parser.add_argument('password',type=str,required=True,help='password cannot be blank')
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.user VALUES('{data['username']}',
                                                       '{data['password']}') """)
        except:
            return{"message":"There is an error connecting to the admin table"},500
        return {"message":"Sucessfully inserted"},201

class Admins():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    @classmethod
    def getAdmin(cls,username):
        result=query(f""" SELECT username,password FROM admin WHERE username='{username}'""",return_json=False)
        if len(result)>0: return Admins(result[0]['username'],result[0]['password'])
        return None
    #@classmethod
    #def getAdminByUsername(cls,username):
     #   result=query(f""" SELECT user_id,username,password FROM user WHERE user_id='{user_id}'""",return_json=False)
      #  if len(result)>0: return Users(result[0]['user_id'],result[0]['username'],result[0]['password'])
       # return None


class Adminlogin(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('username',type=str,required=True,help="username cannot be left blank")
        parser.add_argument('password',type=str,required=True,help="password cannot be left blank")
        data=parser.parse_args()
        admins=Admins.getAdmin(data['username'])
        if Admins and safe_str_cmp(admins.password,data['password']):
            access_token=create_access_token(identity=admins.username,expires_delta=False)
            return {'access_token':access_token},200
        return {"message":"Invalid Credentials"},401
    