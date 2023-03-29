from django.urls import path
from .views import register, logout_user, login_user,password_reset
from django.contrib.auth import views
from .models import Customuser
app_name = "auth"

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('password/reset/',views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="password_reset")
]