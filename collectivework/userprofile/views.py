from django.contrib.auth import authenticate, login as user_login
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        print(username)
        if user is not None:
            user_login(request, user)
            return render(request, 'home.html')
    return render(request, 'login.html')
