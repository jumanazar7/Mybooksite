from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from config import settings
from .models import Customuser


def register(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            return redirect("list")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, "accounts/register.html", {'form': form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("list")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    return render(request, "accounts/login.html", {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("list")


def password_reset(request):
    form = PasswordResetForm()
    if request.method == "POST":
        form =PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            users = Customuser.objects.filter(Q(email=email))
            if users.exists():
                for user in users:
                    subject = "Password Reset Requested"
                    email_template ="accounts/password_reset_text.txt"
                    context_data = {
                        "email" : user.email,
                        'domain':'127.0.0.1:8000',
					    'site_name': 'Website',
                        "user": user,
                        "protocol":"http",
                        "uid":urlsafe_base64_encode(force_bytes(user.pk)),
                        "Token": default_token_generator.make_token(user)
                    }
                    message =render_to_string(email_template,context_data)
                    try:
                        send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse("Invalid header found.")
                    return redirect ("List")
            return render(request,"accounts/password_reset.html",{"form":form})