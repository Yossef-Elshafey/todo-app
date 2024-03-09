from django.urls import path
from . import views

urlpatterns = [
    path("todo", views.TodoView.as_view({"get": "list", "post": "create"})),
    path("todo/<int:pk>", views.SingleTodoView.as_view()),
]
