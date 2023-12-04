from django.views.generic.base import TemplateView
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User, NavBar, InfoSection, CaruselSection, MainStyle, OfferSection, CourseProgram, EndOfCourse, CourseConducted, SpecialOffer, Contacts




def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                User.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, "Ошибка добавление поста")
    else:
        form = UserForm()
        data = {
            "NavBar": NavBar.objects.all(),
            "InfoSection": InfoSection.objects.all(),
            "CaruselSection": CaruselSection.objects.all(),
            "MainStyle": MainStyle.objects.all(),
            "OfferSection": OfferSection.objects.all(),
            "CourseProgram": CourseProgram.objects.all(),
            "EndOfCourse": EndOfCourse.objects.all(),
            "CourseConducted": CourseConducted.objects.all(),
            "SpecialOffer": SpecialOffer.objects.all(),
            "Contacts": Contacts.objects.all(),
            "form": form,
        }
    return render(request, "index.html", {'data': data})