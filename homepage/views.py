from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'sign_in':
            first_name = request.POST['name_register_firstname']
            last_name  = request.POST['name_register_lastname']
            email      = request.POST['name_register_email']
            username   = request.POST['name_register_username']
            password_1 = request.POST['name_register_password1']
            password_2 = request.POST['name_register_password2']

            if password_1 == password_2:
                if User.objects.filter(username=username).exists():
                    return HttpResponse("User Taken")
                elif User.objects.filter(email=email).exists():
                    return HttpResponse("Email Taken")
                else:
                    user = User.objects.create_user(username=username, password=password_1, email=email, first_name=first_name,last_name=last_name)
                    user.save()
                    return HttpResponse("User Created Successfully")

    else:
        return render(request,'home.html')
def login(request):
    pass
