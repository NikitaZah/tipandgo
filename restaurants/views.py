from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import ApplicationForm, LoginForm, CustomUserCreationForm
from .models import *
from ipware import get_client_ip
# Create your views here.


def home(request):
    ip = str(get_client_ip(request))
    if Applicant.objects.filter(ip=ip):
        return render(request, 'restaurants/base.html')
    else:
        return redirect(sign_up)


def sign_up(request):
    ip = str(get_client_ip(request))
    if Applicant.objects.filter(ip=ip):
        return redirect('landing')
    form = ApplicationForm()
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            new_application = form.save(commit=False)
            new_application.ip = ip
            form.save()
            messages.success(request, 'Your application has been successfully sent')
            return redirect('landing')
    context = {'form': form}
    return render(request, 'restaurants/sign_up.html', context)


def registration(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        print('method is post')
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            print('form is valid')
            email = request.POST.get('email')

            if PreRegisteredUser.objects.filter(email=email):
                user = PreRegisteredUser.objects.get(email=email)
                new_user = form.save(commit=False)
                new_user.status = user.status
                form.save()
                messages.success(request, 'successful registration')

            else:
                print('no such user in pre registered')
                messages.error(request, 'Sorry, registration is not available to you. '
                                        'If you would like to use our service for your business, please leave an '
                                        'application')
                return redirect(sign_up)
            return redirect(log_in)
        else:
            print(form.error_messages)
    context = {'form': form}
    return render(request, 'restaurants/registration.html', context)


def log_in(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=str(email), password=str(password))
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.info(request, 'username or password is not correct')
    context = {}
    return render(request, 'restaurants/login.html', context)


def log_out(request):
    logout(request)
    return redirect('login')
