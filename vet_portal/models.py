from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='user/images/profiles', default='user/images/profiles/profile_picture.png',
                                null=True)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)

    def __str__(self):
        return self.user.first_name


class Doctor(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    experience = models.IntegerField()
    price = models.CharField(max_length=10, default=0)
    about = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    qualification = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='vet_portal/images/others', default='user/images/profiles/profile_picture.png',
                                null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    profile = models.ImageField(upload_to='user/images/profiles', default='user/images/profiles/profile_picture.png',
                                null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateTimeField()
    reason = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor.name + '-' + self.patient.name

