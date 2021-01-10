from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader #for template
# Create your views here.
from django.db import connection

from datetime import datetime

from django.contrib import messages


from django.shortcuts import render








# Create your views here.
def rfact(c,r):
    return {i[0]:r[c.description.index(i)] for i in c.description}



def index(request):
    stat="" 
    dl=[]
    print(request.method)
    if request.method=='POST':
      print(request.method)
      nam=request.POST["name"]
      mail=request.POST["emailid"]
      ph=request.POST["mob"]
      pswd=request.POST["pswd"]
     
      

      dateTimeObj = datetime.now()
      sqlb=f"INSERT INTO userdetails(name,email,password,phoneno,datetime)VALUES('{nam}','{mail}','{pswd}','{ph}','{dateTimeObj}')"
      c=connection.cursor()
      c.execute(sqlb)
      # print(dl)
      # n=c.lastrowid
      c.close()
      
     
      messages.success(request, f" Congratulations,Your account has been successfully created !")

      
     



      # return HttpResponseRedirect('/login/',request)  

       
    return render(request,'index.html',{'msg':stat,'userdetails':dl})

def login(request):
  print(request)
  stat=""
  if request.method=='POST':
    unam=request.POST["emailid"]
    pwd=request.POST["pswd"]
    c=connection.cursor()
    c.execute(f"select * from userdetails where email='{unam}'and password='{pwd}'")
    r=c.fetchone()
    c.close()
    if r: #unam=="admin" and pwd=="admin.123":
      request.session['usr']=unam
      return HttpResponseRedirect('/landing/',request)
    stat="Invalid login..try again"
  t=loader.get_template('login.html')
  return HttpResponse(t.render({'msg':stat},request))


def landing(request):
    return render(request,'landingpage.html')