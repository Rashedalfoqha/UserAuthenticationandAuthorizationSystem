from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("users/me/", views.get_current_user, name="get_current_user"),
    path("admin/", views.admin_view, name="admin_view"),
]
