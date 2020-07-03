from flask import Flask,jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resource.user import User,Userlogin
from resource.admin import Admin, Adminlogin
from resource.sch import GetTeacherAvail, Sch, GetTeacherRoom
from resource.seminars import Seminars, RequestStatus, InvalidRequest, AddSeminar
from resource.labs import Labs, AddLab

app=Flask(__name__)
app.config['PROPAGATE_EXPECTATIONS']=True
app.config['JWT_SECRET_KEY']='coscskillup'
api=Api(app)
jwt=JWTManager(app)


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error':'authorization_required',
        'description':'Request does not contain an access token'
    }),401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error':'invalid_token',
        'description':'Signature verification failed.'
    }),401

api.add_resource(Seminars,'/sem')
api.add_resource(RequestStatus,'/reqstat')
api.add_resource(User,'/user')
api.add_resource(Userlogin,'/ulogin')
api.add_resource(Admin, '/admin')
api.add_resource(Adminlogin,'/alogin')
api.add_resource(GetTeacherAvail, '/getavail')
api.add_resource(GetTeacherRoom, '/getroom')
api.add_resource(Sch,'/sch')
api.add_resource(Labs,'/lab')
api.add_resource(InvalidRequest,'/invalidreq')
api.add_resource(AddSeminar,'/addsem')
api.add_resource(AddLab,'/addlab')

if __name__=='__main__':
    app.run(debug=True)
