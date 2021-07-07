from django.shortcuts import render, redirect
from .forms import ProfileForm, UserForm, LoginForm, PatientForm, AppointmentForm, UserUpdateForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Doctor, Patient, Appointment

# Create your views here.


def vet_index(request):
    patients = Patient.objects.filter(user=request.user)
    initial = {'user': request.user}
    form = PatientForm(initial=initial)
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vet_index'))
        else:
            print(form.errors)
    context = {
        'patients': patients,
        'form': form,
    }
    return render(request, 'vetportal/vet_index.html', context)


def signup(request):
    p_form = ProfileForm()
    u_form = UserForm()
    if request.method == 'POST':
        p_form = ProfileForm(request.POST, request.FILES)
        u_form = UserForm(request.POST)
        if p_form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            password = u_form.cleaned_data['password']
            user.set_password(password)
            user.save()
            profile = p_form.save(commit=False)
            profile.user = user
            profile.save()

            return HttpResponseRedirect(reverse('login'))
    context = {
        'p_form': p_form,
        'u_form': u_form,
    }

    return render(request, 'vetportal/signup.html', context)


def basic(request):
    return render(request, 'vetportal/basic.html')


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = User.objects.filter(Q(username=username)).first()
            login(request, user)
            return HttpResponseRedirect(reverse('vet_index'))
    context = {
        'form': form,
    }
    return render(request, 'vetportal/login.html', context)


def update_profile(request):
    user = request.user
    try:
        p_form = ProfileForm(instance=user.user_profile)
    except:
        p_form = ProfileForm()
    u_form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        try:
            p_form = ProfileForm(request.POST, request.FILES, instance=user.user_profile)
        except:
            p_form = ProfileForm(request.POST, request.FILES)

        u_form = UserUpdateForm(request.POST, instance=user)
        if p_form.is_valid() and u_form.is_valid():
            user = u_form.save(commit=False)
            user.save()
            p_form.save()

            return HttpResponseRedirect(reverse('vet_index'))
    context = {
        'p_form': p_form,
        'u_form': u_form,
    }
    return render(request, 'vetportal/update.html', context)


def findbook(request, pk):
    doctors = Doctor.objects.all()
    all_doctors = Doctor.objects.all()
    searched_doctor = request.GET.get('doctor')
    city = request.GET.get('city')
    if searched_doctor:
        doctors = doctors.filter(name=searched_doctor)
        print(searched_doctor)
    if city:
        doctors = doctors.filter(city=city)

    context = {
        'doctors': doctors,
        'pk': pk,
        'all_doctors': all_doctors,
        'searched_doctor': searched_doctor,
        'city': city,
    }
    return render(request, 'vetportal/findbook.html', context)


def doctor(request, d_id, c_id):
    d_details = Doctor.objects.get(id=d_id)
    context = {
        'd_details': d_details,
        'c_id': c_id,
        'd_id': d_id,
    }
    return render(request, 'vetportal/doctorDetails.html', context)


def appointment(request, pk, d_id):
    patient = Patient.objects.get(id=pk)
    initial = {'patient': patient, 'doctor': d_id}
    form = AppointmentForm(initial=initial)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            new_appointment = form.save()
            return HttpResponseRedirect(reverse('slip', args=(new_appointment.pk,)))
        else:
            print(form.errors)
    context = {
        'patient': patient,
        'form': form,
    }
    return render(request, 'vetportal/appointment.html', context)


def remove_patient(request, pk):
    Patient.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('vet_index'))


def slip(request, pk):
    app_query =Appointment.objects.get(id=pk)
    context = {
        'app_query': app_query
    }
    return render(request, 'vetportal/slip.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



