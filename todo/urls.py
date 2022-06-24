from django.urls import path
from todo import views

urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("<int:id>/",views.GetTodoAPIView.as_view(),name="update_todo"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="get_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo"),
    path("login/<email>/<password>",views.LoginApiView.as_view(),name='loginview')
]