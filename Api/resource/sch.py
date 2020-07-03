from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query
from datetime import datetime
import calendar


def getDay(currentTime):
        y=currentTime.year
        d=currentTime.day
        m=currentTime.month
        num=calendar.weekday(y,m,d)
        if num==0:
            return 1
        elif num==1:
            return 2
        elif num==2:
            return 3
        elif num==3:
            return 4
        elif num==4:
            return 5

def getPeriod(currentHour):
        if currentHour==9:
            return 1
        elif currentHour==10:
            return 2
        elif currentHour==11:
            return 3
        elif currentHour==13:
            return 4
        elif currentHour==14:
            return 5
        elif currentHour==15:
            return 6

class Sch(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('faculty_id',type=int,required=True,help='faculty_id cannot be blank')
        """parser.add_argument('sched_id',type=int,required=True,help='sched_id cannot be blank')
        parser.add_argument('day_id',type=int,required=True,help='year cannot be blank')
        parser.add_argument('p_1',type=int,required=True,help='p_1 cannot be blank')
        parser.add_argument('p_2',type=int,required=True,help='p_2 cannot be blank')
        parser.add_argument('p_3',type=int,required=True,help='p_3 cannot be blank')
        parser.add_argument('p_4',type=int,required=True,help='p_4 cannot be blank')
        parser.add_argument('p_5',type=int,required=True,help='p_5 cannot be blank')
        parser.add_argument('p_6',type=int,required=True,help='p_6 cannot be blank')"""
        data=parser.parse_args()
        try:
            return query(f"""SELECT * FROM timetable.sch WHERE faculty_id={data['faculty_id']};""")
        except:
            return{"message":"there is an error connecting to user table."},500

    @jwt_required
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('faculty_id',type=int,required=True,help='faculty_id cannot be blank')
        parser.add_argument('sched_id',type=int,required=True,help='sched_id cannot be blank')
        parser.add_argument('day_id',type=int,required=True,help='year cannot be blank')
        parser.add_argument('p_1',type=int,required=True,help='p_1 cannot be blank')
        parser.add_argument('p_2',type=int,required=True,help='p_2 cannot be blank')
        parser.add_argument('p_3',type=int,required=True,help='p_3 cannot be blank')
        parser.add_argument('p_4',type=int,required=True,help='p_4 cannot be blank')
        parser.add_argument('p_5',type=int,required=True,help='p_5 cannot be blank')
        parser.add_argument('p_6',type=int,required=True,help='p_6 cannot be blank')
        data=parser.parse_args()
        try:
            query(f"""INSERT INTO timetable.user VALUES({data['faculty_id']},
                                                        {data['sched_id']},
                                                        {data['day_id']},
                                                        {data['p_1']},
                                                        {data['p_2']},
                                                        {data['p_3']},
                                                        {data['p_4']},
                                                        {data['p_5']},
                                                        {data['p_6']}) """)
        except:
            return{"message":"There is an error connecting to the schedule table"},500
        return {"message":"Sucessfully inserted"},201

    @jwt_required
    def put(self):
        parser=reqparse.RequestParser()
        parser.add_argument('user_id',type=int,required=True,help="please give user_id")
        
        parser.add_argument('day_id',type=int,required=True,help='day_id cannot be blank')
        parser.add_argument('p_1',type=int,required=True,help='p_1 cannot be blank')
        parser.add_argument('p_2',type=int,required=True,help='p_2 cannot be blank')
        parser.add_argument('p_3',type=int,required=True,help='p_3 cannot be blank')
        parser.add_argument('p_4',type=int,required=True,help='p_4 cannot be blank')
        parser.add_argument('p_5',type=int,required=True,help='p_5 cannot be blank')
        parser.add_argument('p_6',type=int,required=True,help='p_6 cannot be blank')
        data=parser.parse_args()
        try:
            query(f"""UPDATE timetable.sch SET p_1={data['p_1']}, p_2={data['p_2']}, p_3={data['p_3']},
            p_4={data['p_4']}, p_5={data['p_5']}, p_6={data['p_6']} WHERE user_id={data['user_id']} and day_id={data['day_id']}""")
        except:
            return {"message":"there was an error updating the req_status"},500
        return {"message":"successfully updated"},201
            
        

"""class Sch():
    def __init__(self,faculty_id,sched_id, day_id,period):
        self.faculty_id=faculty_id
        self.sched_id=sched_id
        self.day_id=day_id
        self.period=period
        
    @classmethod
    def getSchedule(cls,fac_name):
        currentTime=datetime.datetime.now()
        currentHour=currentTime.hour()
        currentPeriod=getPeriod(currentHour)
        currentDay=getDay(currentTime)

        result=query()

    def getAvailablity(faculty_id):
        currentTime=datetime.datetime.now()
        currentHour=currentTime.hour()
        currentPeriod=getPeriod(currentHour)
        currentDay=getDay(currentTime)

        return avail
        
    @classmethod
    def findTeacherId(facultyname):
        teacher_id=query(f""" #SELECT distinct(faculty_id) FROM timetable.facultyprofile natural join sch s1 WHERE
                #faculty_name LIKE '%'{facultyname}'%' AND f.faculty_id=s.faculty_id AND s.faculty_id=s1.faculty_id 
                # AND s.day_id='{currentDay}'""",return_json=False)
        # return teacher_id
        

class GetTeacherAvail(Resource):
    @jwt_required
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('fac_name',type=str,required=True,help="give teacher name")
        data=parser.parse_args()
        currentTime=datetime.now()
        currentHour=currentTime.hour
        currentPeriod=getPeriod(currentHour)
        currentDay=getDay(currentTime)
        try:
            return query(f"""SELECT sch.p_{currentPeriod} as avail FROM timetable.facultyprofile JOIN timetable.sch WHERE
            faculty_name LIKE '%'{data['fac_name']}'%' AND facultyprofile.faculty_id=sch.faculty_id
            AND day_id={currentDay}""",return_json=True)
            
            
        except:
            return{"message":"there is an error connecting to database."},500

         
      
 
class GetTeacherRoom(Resource):
    @jwt_required
    def get(self):
        try:
            return query(f"""SELECT * FROM timetable.schdum;""")
            
        except:
            return{"message":"there is an error connecting to database."},500
