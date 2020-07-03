# cosc application
TEACHER TIME TABLE MANAGEMENT SYSYTEM:

The REST API is deployed to heroku

Link:https://internship-team-2.herokuapp.com/

Everybody can use the below endpoints to access the tables in the database

1)/ulogin - takes a JSON object with 'username' and 'password' and gives back JWT if exists in User table. The JWT shall be used to access all the end points. For all the endpoints an Authorization Header should be included with value 'Bearer '.

2)/user(GET) -takes a JSON object with 'user_id'.

3)/user(POST)-POST into user table.

4)/sem(GET)-takes a JSON object with 'availability'=0

5)/sem(POST)-POST into seminars Table.

6)/reqstat(GET)-takes a JSON object whose req_status is pending

7)/reqstat(PUT)-takes a JSON object with 'user_id' and updates the req_status as approved .'user_id' is must.

8)/admin(GET)-takes an JSON object with 'admin_id'.'admin_id' is must.

9)/admin(POST)-POST into admin table.'username','password' are must.

10)/alogin(GET)-takes a JSON object with 'username' and 'password' and gives back JWT if exists in admin table. The JWT shall be used to access all the end points. For all the endpoints an Authorization Header should be included with value 'Bearer '.

def getDay(currentTime): y=currentTime.year d=currentTime.day m=currentTime.month num=calendar.weekday(y,m,d) if num==0: return 1 elif num==1: return 2 elif num==2: return 3 elif num==3: return 4 elif num==4: return 5

def getPeriod(currentHour): if currentHour==9: return 1 elif currentHour==10: return 2 elif currentHour==11: return 3 elif currentHour==13: return 4 elif currentHour==14: return 5 elif currentHour==15: return 6

11)the above two functions illustrates about the current hour of a faculty and the period too.

12)/sch(GET)-takes JSON object 'faculty_id','sched_id','day_id','p_1','p_2','p_3','p_4','p_5','p_6'.Gives the details if faculty_id given. 'faculty_id','sched_id','day_id','p_1','p_2','p_3','p_4','p_5','p_6' are must.

13)/sch(POST)-POST into the sch table.

14)/sch(PUT)-takes JSON objects 'user_id','sched_id','day_id','p_1','p_2','p_3','p_4','p_5','p_6'.Updates these in the sch table . 'user_id','sched_id','day_id','p_1','p_2','p_3','p_4','p_5','p_6' are must.

15)/getavail(GET)- takes an JSON object 'fac_name' and gives the details about that faculty current hour,current day,current time,current period.''fac_name' must.

16)/lab(GET) - gets the information related to labs by checking their 'availability'=0

17)/lab(POST)-POST into labs table.

18)/getroom(GET): Gives all the details present in sch table ,so that the user can directly see the faculty details easily

19)/invalidreq(PUT): It puts the msg like "invalid Request" ."user_id" is must.

20)/addsem(POST): It creates a new entry in the db with the following attributes -"seminar_name","sem_no","availability"."seminar_name","sem_no","availability" are must.

21)/addlab(POST): It creates a new entry in the db with the following attribtes -     "lab_no","building_no","capacity","availibility"."lab_no","building_no","capacity","availibility" are must.
