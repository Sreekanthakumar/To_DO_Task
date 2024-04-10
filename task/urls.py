from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("addlist",views.addlist,name="addlist"),
    path("completed",views.completed,name="completed"),
    path("delete/<id>",views.delete,name="delete"),
    path("edit/<id>",views.edit,name="edit"),
    path("incompleted",views.incompleted,name="incompleted"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout", views.signout,name="signout"),
    path("update/<id>",views.update,name="update")
]
