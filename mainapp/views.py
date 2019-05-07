from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LogInForm
from .models import Profile
# Create your views here.

def index(request):
    return render(request, 'mainapp/homePage.html')

def contact(request):
    return render(request, 'mainapp/basic.html', {'values': ['Если у вас остались вопросы звоните по номеру:', 'Телефон: 8 747 777 77 77', 'Email: dmitry.k@gmail.com']})    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            profile = Profile()
            profile.user = user
            profile.name_company = form.cleaned_data.get("fio")
            profile.save()
            #login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'mainapp/signup.html', {'form':form})

def login(request):
    context = {'error':''}
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if request.POST.get('form','') =='login':
            username = request.POST.get('login','')
            password = request.POST.get('password','')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user = request.user
                return redirect('index')
            else:
                context["error"] = "Неверное имя или пароль"
                return render(request, 'index.html', context)

    return render(request, 'mainapp/signup.html', {'form':form})
