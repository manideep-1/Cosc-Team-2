from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class Labs(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT * FROM timetable.labs WHERE availibility='0'""")
        except:
            return {"message":"there was an error retrieving the data"},500

    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="User_id name cannot be left blank!")
        parser.add_argument('room_id',type=int, required=True,help="room number cannot be left blank!")
        parser.add_argument('purpose',type=str,required=True,help="purpose can't be left blank!")
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.requests(user_id, room_id, purpose, req_status)
                                VALUES({data['user_id']},{data['room_id']},
                                            '{data['purpose']}','pending')""")
        except:
            return {"message": "An error occurred."}, 500
        return {"message": "successfully added request."}, 201

        

    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('lab_no',type=int,required=True,help="please give seminar hall number")
        parser.add_argument('avail',type=int,required=True,help="please give availibility as 0 or 1")
        data=parser.parse_args()
        try:
            query(f"""UPDATE timetable.labs SET availibility={data['avail']} WHERE lab_no={data['lab_no']}""")
        except:
            return {"message":"there was an error updating the req_status"},500
        return {"message":"successfully updated"},201


class AddLab(Resource):
    @jwt_required
    def post(self):
            parser=reqparse.RequestParser()
            parser.add_argument('lab_no',type=int,required=True,help='lab_no cannot be blank')
            parser.add_argument('building_no',type=int,required=True,help='building no cannot be blank')
            parser.add_argument('capacity',type=int,required=True,help='availibility cannot be blank')
            parser.add_argument('availibility',type=int,required=True,help='availibility cannot be blank')
            data=parser.parse_args()
            try:
                query(f"""INSERT INTO timetable.seminars VALUES({data['lab_no']},
                                                            {data['building_no']},
                                                            {data['capacity']},
                                                            {data['availability']}
                                                            ) """)
            except:
                return{"message":"There is an error connecting to the db"},500
            return {"message":"Sucessfully inserted"},201