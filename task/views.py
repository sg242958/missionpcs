from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Days
from .forms import DaysForm
# Create your views here.


# This is register function
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        users = request.POST['username']
        email = request.POST['email']
        if request.POST['password'] == request.POST['confirm_password'] and len(request.POST['password']) > 8:
            try:
                user = User.objects.get(username=users)
                print(user)
                return render(request, 'signup.html', {'error': 'Username already exist, Please Try Again'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=users, password=request.POST['password'])
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
                messages.success(request, "Your Account created Successfully")
                return redirect('/')
        else:
            return render(request, 'signup.html', {'errors': 'Password not Match and your password length should be 8 character , Please Try Again'})
    return render(request, 'signup.html')

# This is login function
def Login(request):
    if request.session.has_key('is_logged'):
        return render(request, 'timetable.html')
    if request.method == 'POST':
        uname = request.POST['uname']
        psw = request.POST['psw']
        user = authenticate(username=uname, password=psw)
        if user is not None:
            login(request, user)
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
            request.session['is_logged'] = 'shivam'
            return redirect('/time_table')
        else:
            return render(request, 'login.html', {'error': "Do not match login detail"})
    else:
        return render(request, 'login.html')

# This is logout function
login_required('/login')
def Logout(request):
    logout(request)
    del request.session
    return render(request, 'login.html')


# This is timetable webpage function
login_required('/login')
def time_table(request):
    if request.session.has_key('is_logged'):
        data = Days.objects.all()
        return render(request, 'timetable.html', {'data': data})
    return render(request, 'login.html')

# This function is used for edit
login_required('/login')
def edit(request, id):
    if request.method == 'POST':
        data = Days.objects.get(pk=id)
        form = DaysForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Days.objects.get(pk=id)
        form = DaysForm(instance=data)
    return render(request, 'edit.html', {'form': form})

# This is used for delete row
def delete(request, id):
    if request.method == 'POST':
        dele = Days.objects.get(pk=id)
        dele.delete()
        return redirect('/time_table')

# This is used for add row in timetable
login_required('/login')
def add(request):
    if request.method == 'POST':
        form = DaysForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DaysForm()
    return render(request, 'add.html', {'form': form})