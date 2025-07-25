from django.shortcuts import render,redirect,get_object_or_404
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
    obj = subject.objects.filter(subject_name__range=("a", "n"))
    context ={
        "y" : obj
    }
    print(obj)
    for i in obj:
        print(i.student_id.firstname)
    return render(request,"subject.html",context)

def edit_subject(request,id):
    sub = get_object_or_404(subject, id=id)
    students = student.objects.all()
    if request.method == "POST":
        stid = request.POST['stid']
        sub.student_id = student.objects.get(id=stid)
        sub.subject_name = request.POST['subname']
        sub.chapter_count = request.POST['chapcount']
        sub.desc = request.POST['desc']
        sub.save()
        return redirect('h1')
    else:
        s1 = subject.objects.get(id=id)
        context ={
            "i" : s1
        }
        return render(request,"edit_subject.html", {'i': sub, 'students': students})
    
def add_subject(request):
    sub1 = subject()
    print(sub1)
    students1 = student.objects.all()
    if request.method == "POST":
        stid = request.POST['stid']
        sub1.student_id = student.objects.get(id=stid)
        sub1.subject_name = request.POST['subname']
        sub1.chapter_count = request.POST['chapcount']
        sub1.desc = request.POST['desc']
        sub1.save()
        
        return redirect('h1')
    else:
        return render(request,"add_subject.html",{'i': sub1, 'students1': students1})
    
def delete_subject(request,id):
   d2 = subject.objects.get(id=id)
   d2.delete()
   return redirect('home1')