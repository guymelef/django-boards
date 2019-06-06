from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("settings/account/", views.UserUpdateView.as_view(), name='my_account'),
]