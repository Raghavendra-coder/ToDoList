from django.contrib import admin
from .models import Profile, Doctor, Patient, Appointment

# Register your models here.


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'date', 'reason')

admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment, AppointmentAdmin)
