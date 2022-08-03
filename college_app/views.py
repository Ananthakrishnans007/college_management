from multiprocessing import context
import os
import re
from django.shortcuts import render,redirect
from . models import*
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request,'index.html')

def login_page(request):
    return render (request,'login.html')


def signup(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render (request,'signup.html',context)


@login_required(login_url='user_login')
def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_page')
    return render(request,'admin/home.html')

@login_required(login_url='user_login')
def tutor_home(request):
    return render(request,'tutor/home.html')


@login_required(login_url='user_login')
def add_course(request):
        return render(request,'admin/add_course.html')

@login_required(login_url='user_login')
def add_student(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render(request,'admin/add_student.html',context)
            



def sign_up(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        address=request.POST['address']
        gender=request.POST['gender']
        username=request.POST['uname']
        email=request.POST['email']
        phone=request.POST['phone']
        sel=request.POST['sel']
        password=request.POST['psw']
        c_password=request.POST['cpsw']

        

        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!!!!!!')
                return redirect('signup') 

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!!!!!!')
                return redirect('signup') 

            else:
                user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=username,
                    email=email,
                    password=password) 
                user.save() 

                u=User.objects.get(id=user.id)
                course=Course.objects.get(id=sel)
                member=Tutor(Address=address,Gender=gender,Course=course,Phone=phone,user=u)
                if len(request.FILES) != 0:
                    Tutor.Image=request.FILES['file']


                member.save()

                return redirect('login_page') 
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            return redirect('signup') 
    else:
        return render(request,'signup.html')


def user_login (request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['psw']
        user=auth.authenticate(username=username,password=password)
        request.session["uid"]=user.id
        
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                Name=user.first_name +" "+ user.last_name
                messages.info(request, f'Welcome {Name}')
                return redirect('tutor_home')

        else:
            messages.info(request, 'Invalid Username or Password. Try Again.')
            return redirect('login_page')
    else:
        return redirect('login_page')



 

@login_required(login_url='user_login')
def course(request):
    if request.method=='POST':
        course_name=request.POST['cname']    
        fee=request.POST['fee']
        crs=Course()
        crs.Course_Name=course_name
        crs.Fee=fee
        crs.save()
        return redirect('show_course')

@login_required(login_url='user_login')
def student(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        age=request.POST['age']
        date=request.POST['date']
        phone=request.POST['phone']
        sel=request.POST['sel']
        course=Course.objects.get(id=sel)
        std=Student()
        std.Student_Name=name
        std.Address=address
        std.Age=age
        std.Join_date=date
        std.Course=course
        std.Phone=phone
        std.save()
        return redirect('show')
        
@login_required(login_url='user_login')
def show(request):
    student=Student.objects.all()
    courses=Course.objects.all()
    
    
    return render(request,'admin/show_student_details.html',{'x':student,'y':courses})



@login_required(login_url='user_login')
def show_student(request):
    to=Tutor.objects.get(user=request.user)
    name=to.Course
    student=Student.objects.filter(Course=name)
    return render(request,'tutor/show_student.html',{'x':student})





@login_required(login_url='user_login')
def show_course(request):
    course=Course.objects.all()
    return render(request,'admin/show_course.html',{'x':course})


@login_required(login_url='user_login')
def edit_course(request,pk):
    if request.method=="POST":
        course=Course.objects.get(id=pk)
        course.Course_Name=request.POST['C_Name']
        course.Fee=request.POST['fee']
        course.save()
        return redirect('show_course')
 


@login_required(login_url='user_login')
def delete_course(request,pk):
    course=Course.objects.get(id=pk)
    course.delete()
    return redirect('show_course')


@login_required(login_url='user_login')
def edit_student(request,pk):
    if request.method=='POST':
        std=Student.objects.get(id=pk)
        std.Student_Name=request.POST['name']
        std.Address=request.POST['address']
        std.Age=request.POST['age']
        temp=request.POST['date']

        if temp =="":
            std.Join_date=std.Join_date
        else:
            std.Join_date=request.POST['date']

        std.Phone=request.POST['phone']

        sel=request.POST['sel']
        course=Course.objects.get(id=sel)

        std.Course=course

        std.save()
        return redirect('show')





@login_required(login_url='user_login')
def show_tutor(request):
    tutor=Tutor.objects.all()
    return render(request,'admin/show_tutor.html',{'x':tutor})

@login_required(login_url='user_login')
def profile(request):
   tutor=Tutor.objects.filter(user=request.user)
   courses=Course.objects.all()

   return render(request,'tutor/profile.html',{'x':tutor,'y':courses})


def edit_profile(request):
    if request.method=='POST':
        user=User.objects.get(id=request.user.id)
        tutor=Tutor.objects.get(user=request.user)

        if len(request.FILES) != 0:
            if len(tutor.Image) > 0  :
                os.remove(tutor.Image.path)
                
            tutor.Image=request.FILES['file'] 

        


        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        tutor.Address=request.POST['address']
        tutor.Gender=request.POST['gender']


        username=request.POST['username']
        user.username =username
                 

        tutor.Phone=request.POST['gender']
        user.email=request.POST['email']
        tutor.Phone=request.POST['phone']

        sel=request.POST['sel']
        course=Course.objects.get(id=sel)
        tutor.Course=course
        user.save()
        tutor.save()
        return redirect('profile')
        
def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('index')
           
def test(request):
    return render(request,request,'test.html')
        





    
    
           
    












