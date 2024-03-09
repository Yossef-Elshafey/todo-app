from django.urls import path
from . import views

urlpatterns = [
        path("sign-up", views.SignUp.as_view({"post":"create"})),
        path("login", views.Login.as_view({"post":"create"}))
        ]
