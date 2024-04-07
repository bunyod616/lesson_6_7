from django.shortcuts import render, redirect
from django.views import View
from .models import Student
from django.http import HttpResponse
from django.contrib.auth.models import User
class StudentListView(View):
    def get(self, request):
        search = request.GET.get('search')

        if not search:
            students = Student.objects.all()
            context = {
                'student': students,
                'search': search
            }
            return render(request, 'student.html',  {'talabalar': students},)
        else:
            students = Student.objects.filter(first_name__icontains=search)
            if students:
                context = {
                    'student': students,
                    'search': search
                }
                return render(request, 'student.html', context)
            else:
                return HttpResponse('<h1>No student found</h1>')


class StudentView(View):
    def get(self, request):
        return render(request, 'index.html')


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        user = User(first_name=first_name, last_name=last_name, username=username, email=email,)
        user.set_password(password_1)
        user.save()
        return redirect("landing")

class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.filter(username=username, password=password)
        if user:
            print("<<<<<<<<<<<<< Sucsesfull >>>>>>>>>>>>")
            return redirect("landing")

        else:
            print("<<<<<<<<<<<<< Error >>>>>>>>>>>>")
            return render(request, "user_not_found.html")