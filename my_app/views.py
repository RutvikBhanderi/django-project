from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import student, subject

def demo(request):
    obj = student.objects.all()
    context ={
        "x" : obj
    }
    print(context)
    return render(request,"first.html",context)

def contact_us(request):    
    return HttpResponse("you are in contact-us")

def about_us(request):
    return HttpResponse("you are in about-us")  

def add_student(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        Email = request.POST['email']
        Phone = request.POST['phone']
        City = request.POST['city']
        img = request.FILES['image']
        obj2 = student()
        obj2.firstname=fname
        obj2.lastname=lname
        obj2.age=age
        obj2.email=Email
        obj2.phone=Phone
        obj2.city=City
        obj2.image=img
        obj2.save()
        print(request.POST['fname'])
        return redirect('home')
    else:
        return render(request,"add_student.html")

def edit_student(request,id):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        Email = request.POST['email']
        Phone = request.POST['phone']
        City = request.POST['city']
        obj2 = student.objects.get(id=id)
        obj2.firstname=fname
        obj2.lastname=lname
        obj2.age=age
        obj2.email=Email
        obj2.phone=Phone
        obj2.city=City
        obj2.save()
        print(request.POST['fname'])
        return redirect('home')
    else:
        s1 = student.objects.get(id=id)
        context ={
            "b" : s1
        }
        return render(request,"edit_student.html",context)

def delete_student(request,id):
   d1 = student.objects.get(id=id)
   d1.delete()
   return redirect('home')

### subject table:

def demo1(request):
    obj = subject.objects.all()
    context ={
        "y" : obj
    }
    print(obj)
    for i in obj:
        print(i.student_id.firstname)
    return render(request,"subject.html",context)

def edit_subject(request,id):
    if request.method == "POST":
        stdid = request.POST['stid']
        subname = request.POST['subname']
        chapcount = request.POST['chapcount']
        desc = request.POST['desc']
        obj2 = subject.objects.get(id=id)
        obj2.student_id = stdid
        obj2.subject_name = subname
        obj2.chapter_count = chapcount
        obj2.desc = desc
        obj2.save()
        return redirect('home1')
    else:
        s1 = subject.objects.get(id=id)
        context ={
            "i" : s1
        }
        return render(request,"edit_subject.html",context)
    
def add_subject(request):
    if request.method == "POST":
        stdid = request.POST['stid']
        subname =request.POST['subname']
        chapcount =request.POST['chapcount']
        desc =request.POST['desc']
        obj2 = subject.objects.get()
        obj2.student_id = stdid
        obj2.subject_name = subname
        obj2.chapter_count = chapcount
        obj2.desc = desc
        obj2.save()
        return redirect('home1')
    else:
        return render(request,"add_subject.html")
    
def delete_subject(request,id):
   d2 = subject.objects.get(id=id)
   d2.delete()
   return redirect('home1')