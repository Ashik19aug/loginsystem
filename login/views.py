from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout



def login(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = authenticate(request, email=email,password=password)

		if user is not None:
			login(request, user)
			return redirect('/login/home/')
		else:
			return render(request,'login/login.html')

	return render(request,'login/login.html')



def home(request):
	return render(request,"login/home.html")
