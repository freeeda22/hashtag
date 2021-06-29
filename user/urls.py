from django.contrib.auth import views
from . import views
from django.urls import path


urlpatterns = [
    path('signup/', views.SignupAPIView.as_view(),name="signup_user"),
    path('login/',views.LoginAPIView.as_view(), name="login"),

]