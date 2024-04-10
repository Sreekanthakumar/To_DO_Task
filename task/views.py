from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import list 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

def home(request):
    return HttpResponse("HELLO WORLD")

@login_required(login_url='signin')
def addlist(request):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        due = request.POST.get('due')
        list.objects.create(user = request.user,taskname = taskname,due = due,)
    all_lists = list.objects.filter(user=request.user,status=0)
    context ={
        'list': all_lists
    }
    return render(request,"task/add.html",context)

def completed(request):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        due = request.POST.get('due')
        list.objects.create(user = request.user,taskname = taskname,due = due,)
    all_lists = list.objects.filter(user=request.user,status=1)
    context ={
        'list': all_lists
    }
    return render(request,"task/add.html",context)



def delete(request,id):
    list.objects.get(id=id).delete()
    return redirect("addlist")

def edit(request,id):
    changelist = list.objects.get(id = id)
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        due = request.POST.get('due')
        changelist.taskname = taskname
        changelist.due = due
        changelist.save()
        return redirect('addlist')
    return render(request,'task/edit.html',{'changelist':changelist})

def incompleted(request):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        due = request.POST.get('due')
        list.objects.create(user = request.user,taskname = taskname,due = due,)
    all_lists = list.objects.filter(user = request.user,status=0)
    return render(request,"task/add.html",{'list':all_lists})


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            User.objects.create_user(
            username = username,
            password = password
        )
    messages.add_message(request, messages.SUCCESS, "sucessfully sigined")
    return render(request,"task/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = authenticate(username = username,password = password)
        if data is not None:
            login(request,data)
            return redirect('addlist')
        messages.add_message(request, messages.SUCCESS, "sucessfully logined")
    return render(request,"task/signin.html")

def signout(request):
    logout(request)
    return redirect('signin')

def update(request,id):
    get_list= list.objects.get(user=request.user,id=id)
    get_list.status = True
    get_list.save()
    return redirect('addlist')

        

