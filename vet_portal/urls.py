from django.urls import path
from . import views

urlpatterns = [
    path("", views.vet_index, name="vet_index"),
    path("signup", views.signup, name="signup"),
    path("basic", views.basic, name="basic"),
    path("login", views.user_login, name="login"),
    path("update", views.update_profile, name="update"),
    path("findbook/<pk>", views.findbook, name="findbook"),
    path("doctor/<d_id>/<c_id>", views.doctor, name="doctor"),
    path("appointment/<pk>/<d_id>", views.appointment, name="appointment"),
    path("remove_patient/<pk>", views.remove_patient, name="remove_patient"),
    path("slip/<pk>", views.slip, name="slip"),
    path("logout", views.user_logout, name="user_logout"),
]
