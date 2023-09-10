from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
   ## return HttpResponse('this is Index pages')
   return render(request,'index.html')
   
    
def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        user=Register.objects.filter(username=username1,password=password1).first()
        if user is not None:
            # messagese.success(request,"Successfully Logged In")
            request.session['username']=username1
            messages.add_message(request, messages.SUCCESS, "Successfully Logged In!!")
            return redirect('/home')
        else:
           
            messages.add_message(request, messages.ERROR, "Please enter correct email or password!!")
            return redirect('/login')
    return render(request,'login.html')
 

    
def logout(request):
        del request.session['username']
        messages.add_message(request, messages.SUCCESS, "Logout Successfully!!")
        return redirect('/index')
      
def header(request):
    return render(request,'header.html')

   
def about(request):
    return render(request,'about.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        mobile_no=request.POST['mobile_no']
        email=request.POST['email']
        password=request.POST['password']
        data=Register.objects.create(username=username,mobile_no=mobile_no,email=email,password=password)
        return redirect('/login')
    else:
        return render(request,'index.html')
    
# def contact(request):
#     if request.method=='POST':
#         name1=request.POST['name']
#         email1=request.POST['email']
#         message1=request.POST['message']
#         data=Contact.objects.create(name=name1,email=email1,message=message1)
#         return redirect('/login')
    
         
# def contact_details(request):
#     data=Contact.objects.all()
#     return render(request,'contact_details.html',{'title':'Contact List','data':data})
    


    
    
def user_list(request):
    # data=Register.objects.all()
    # data=Register.objects.filter(mobile_no=7903493441).values()
    # data=Register.objects.get(id=1)
    data=Register.objects.all()
    return render(request,'user_list.html',{'title':'User List','data':data})

def delete_user(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect('/userlist')
def editUser(request,id):
    data=Register.objects.filter(id=id).first()
    return render(request,'editUser.html',{'data':data})
def update_user(request):
    username=request.POST['username']
    mobile_no=request.POST['mobile_no'] 
    email=request.POST['email'] 
    password=request.POST['password'] 
    editid=request.POST['editid'] 
    data=Register.objects.get(id=editid)
    data.username=username
    data.mobile_no=mobile_no
    data.email=email
    data.password=password
    data.save()
    return redirect('/userlist')

def home(request):
    return render(request,'home.html')

def notes(request):
    return render(request,'notes.html')
def homework(request):
    return render(request,'homework.html')
def todo(request):
    return render(request,'todo.html')
def calculator(request):
    return render(request,'calculator.html')
