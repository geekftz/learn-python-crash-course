# from django.contrib.auth.views import login
from django.urls import path, include
from django.contrib.auth import login
# from django.contrib.auth.views import login

from django.contrib.auth.views import LoginView

urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login')
    # path('login/', LoginView.as_view(template_name='learning_logs/base.html'), name="login")
]
