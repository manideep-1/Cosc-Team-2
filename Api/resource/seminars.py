from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class Seminars(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT * FROM timetable.seminars WHERE availibility='0'""")
        except:
            return {"message":"there was an error retrieving the data"},500

    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="User_id name cannot be left blank!")
        parser.add_argument('room_id',type=int,required=True,help="room_id cannot be left blank!")
        parser.add_argument('club_name',type=str,required=True,help="club_name cannot be left blank!")
        parser.add_argument('purpose',type=str,required=True,help="fine can't be left blank!")
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.requests(user_id, room_id, club_name, purpose, req_status)
                                VALUES({data['user_id']},{data['room_id']},'{data['club_name']}',
                                            '{data['purpose']}','pending')""")
        except:
            return {"message": "An error occurred."}, 500
        return {"message": "successfully added request."}, 201
    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('sem_no',type=int,required=True,help="please give seminar hall number")
        parser.add_argument('avail',type=int,required=True,help="please give availibility as 0 or 1")
        data=parser.parse_args()
        try:
            query(f"""UPDATE timetable.seminars SET availibility={data['avail']} WHERE sem_no={data['sem_no']}""")
        except:
            return {"message":"there was an error updating the req_status"},500
        return {"message":"successfully updated"},201

            
    
class RequestStatus(Resource):
    
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT * FROM timetable.requests WHERE req_status='pending'""")
        except:
            return {"message":"There was an error displaying the data"},500

    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="please give user_id")
        data=parser.parse_args()
        try:
            query(f"""UPDATE timetable.requests SET req_status='Approved' WHERE user_id={data['user_id']}""")
        except:
            return {"message":"there was an error updating the req_status"},500
        return {"message":"successfully updated"},201

class InvalidRequest(Resource):
    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="please give user_id")
        data=parser.parse_args()
        try:
            query(f"""UPDATE timetable.requests SET req_status='Invalid' WHERE user_id={data['user_id']}""")
        except:
            return {"message":"there was an error updating the req_status"},500
        return {"message":"successfully updated"},201

class AddSeminar(Resource):
    @jwt_required
    def post(self):
            parser=reqparse.RequestParser()
            parser.add_argument('seminar_name',type=str,required=True,help='user_id cannot be blank')
            parser.add_argument('sem_no',type=int,required=True,help='dept_id cannot be blank')
            parser.add_argument('availability',type=int,required=True,help='year cannot be blank')
            data=parser.parse_args()
            try:
                query(f"""INSERT INTO timetable.seminars VALUES('{data['seminar_name']}',
                                                            {data['sem_no']},
                                                            {data['availability']}
                                                            ) """)
            except:
                return{"message":"There is an error connecting to the req_status"},500
            return {"message":"Sucessfully inserted"},201
            