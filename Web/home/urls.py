from django.urls import path
from . import views

urlpatterns = [
    path('loginpage/',views.loginpage,name='loginpage'),
    path('login/',views.login,name='login'),
    path('display/',views.display,name='display'),
    path('show/',views.show,name='show'),
    path('labshow/',views.labshow,name='labshow'),
    path('labdis/',views.labdis,name='labdis'),
    path('addlab/',views.addlab,name='addlab'),
    path('form/',views.form,name='form'),
    path('sh/',views.sh,name='sh'),
    path('showlab/',views.showlab,name='showlab'),
    path('logout/',views.logout,name='logout'),
    path('back/',views.back,name='back'),
    path('showsem/',views.showsem,name='showsem'),
    path('asktt/',views.asktt,name='asktt'),
    path('tt',views.tt,name='tt')
]