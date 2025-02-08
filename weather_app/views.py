from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from .models import *
from django.http import JsonResponse

def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		if not CustomUser.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'خطا در شناسایی کاربر')
			return redirect('/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "خطا در شناسایی کاربر")
			return redirect('/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('/home/', name=username)
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')


def aqi(request):
    if request.method == "POST":
        try:
            import json
            data = json.loads(request.body)
            aqi_value = data.get('aqi_value', 0)
            #request.session['aqi_value'] = data.get('aqi_value', 0)
            #AQIValue.objects.all().delete()  # Remove old values 
            AQIValue.objects.create(value=aqi_value)
            return JsonResponse({"message": "AQI value stored", "aqi_value": aqi_value}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    
    #aqi_value = request.session.get('aqi_value', 0)
    #context = {
	#	'aqi_value': aqi_value
    #}
    aqi_entry = AQIValue.objects.last()
    aqi_value = aqi_entry.value if aqi_entry else 0
    return render(request, 'aqi1.html', {"aqi_value": aqi_value})


def logout_page(request):
     logout(request)
     return redirect('login_page')