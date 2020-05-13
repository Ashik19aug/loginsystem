from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password

@csrf_exempt

def login(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		
		
		user = User.objects.get(email=email)
		if user.check_password(password):
			messages.info(request,'successfully Login')
			return redirect('/login/home/')
		else: 
			return render(request,"login/home.html")
	return render(request,'login/login.html')




def home(request):
	return render(request,"login/home.html")
