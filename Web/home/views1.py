from django.shortcuts import render
from django.http import HttpResponse

import requests
# Create your views here.
admintoken=''
username=''

def loginpage(request):
    return render(request,'coscc.html')

def logout(request):
    return render(request,'coscc.html')

def login(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    global admintoken
    data= requests.get('https://internship-team-2.herokuapp.com/alogin',data={"username":username,"password":password})
    data=data.json()
    print(data)
    admintoken=data["access_token"]
    context={"data":data}
    return render(request,'first.html')

def labshow(request):
    global admintoken
    data=requests.get('https://internship-team-2.herokuapp.com/labs',headers={'Authorization':'Bearer {}'.format(admintoken)})
    data=data.json()
    print(data)  
    context={"data":data}
    return render(request,"labshow.html",context)

def labdis(request):
    global admintoken
    lab_no=request.POST.get('lab_no','')
    building_no=request.POST.get('building_no','')
    capacity=request.POST.get('capacity','')
    availability=request.POST.get('availability','')
    data= requests.put('https://internship-team-2.herokuapp.com/addlab',headers={'Authorization':'Bearer {}'.format(admintoken)},data={"lab_no":lab_no,"building_no":building_no,"capacity":capacity,"availability":availability})
    data=data.json()
    print(data)
    context={"data":data}
    return render(request,"labdis.html",'')

def show(request):
    global admintoken
    data= requests.get('https://internship-team-2.herokuapp.com/reqstat',headers={'Authorization':'Bearer {}'.format(admintoken)})
    data=data.json
    context={"data":data}
    return render(request,'demo.html',context)

def display(request):
    global username
    global admintoken
    user_id=request.POST.get('user_id')
    data= requests.put('https://internship-team-2.herokuapp.com/reqstat',headers={'Authorization':'Bearer {}'.format(admintoken)},data={"user_id":user_id})
    data=data.json()
    print(data)
    context={"data":data}
    return render(request,'display.html',context)

def sh(request):
    global username
    global admintoken
    user_id=request.POST.get('user_id')
    data= requests.put('https://internship-team-2.herokuapp.com/reqstat',headers={'Authorization':'Bearer {}'.format(admintoken)},data={"user_id":111})
    data=data.json()
    context={"data":data}
    return render(request,'back.html',context)

def back(request):
    return render(request,'first.html')

def form(request):
    return render(request,'labsss.html')
                                                                                                                                                 
def addlab(request):
    global admintoken
    print(admintoken)
    lab_no=request.POST.get('lab_no','')
    building_no=request.POST.get('building_no','')
    capacity=request.POST.get('capacity','')
    availibility=request.POST.get('availibility','')
    token=requests.post('https://internship-team-2.herokuapp.com/addlab',data={"lab_no":lab_no,"building_no":building_no,"capacity":capacity,"availibility":availibility})
    data=token.json()
    print(data)
    return HttpResponse(str(data["message"]))

def showlab(request):
    global admintoken
    data=requests.get('https://internship-team-2.herokuapp.com/showlab')
    data=data.json()
    print(data)
    context={"data":data}
    return render(request,'hey.html',context)

def showsem(request):
    global admintoken
    data=requests.get('https://internship-team-2.herokuapp.com/showsem')
    data=data.json()
    print(data)
    context={"data":data}
    return render(request,'display.html',context)

def asktt(request):
    return render(request,'time1.html')
    
def tt(request):
    global admintoken
    data=requests.get('https://internship-team-2.herokuapp.com/tt')
    data=data.json()
    print(data)
    context={"data":data}
    return render(request,'time.html',context)
