from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
import random
from django.contrib.auth import logout as alogout# Ensure this is imported

def logout(request):
    if request.method == "POST":
        alogout(request)
        return render(request,'index.html')  # Redirects back to your login/signup page
   # Safety redirect

images ={
    1: 'https://i.pinimg.com/736x/c0/c4/c9/c0c4c9a6aed4a15c29c6362881aba7ef.jpg',
    2:'https://i.pinimg.com/736x/78/8b/37/788b376809529fa605eaa7cbf7050f7f.jpg',
    3: 'https://i.pinimg.com/736x/72/c0/6e/72c06e850eeb396da5c991cf18aa3a2c.jpg',
    4 : 'https://i.pinimg.com/736x/71/55/a3/7155a3341ab2a092374a202b35600791.jpg',
    5 : 'https://i.pinimg.com/originals/7b/e1/ea/7be1ea583c9ae66b28efd56ea15edd25.png',
    6: 'https://i.pinimg.com/736x/b1/65/d0/b165d047203897cc1829c79591080671.jpg',
    7:'https://i.pinimg.com/736x/a1/70/3d/a1703d845cc154163fbd95b2dc50d47a.jpg' ,
    8: 'https://i.pinimg.com/736x/34/11/4c/34114cfe0a91d0f92eb8490d3e0eb68d.jpg'
}


def index(request):
    if request.method == "POST":
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        action = data.get("action")

        if action == "signup":
            # Basic Signup Logic
            if User.objects.filter(username=email).exists():
                messages.error(request, "User already exists")
            else:
                user = User.objects.create_user(username=email, password=password)
                login(request, user)
                n = random.choice(range(1,9))
            
                # The context dictionary maps the 'variable_name' used in HTML to the Python variable
                return render(request, 'image.html', {'img_uri': images[n]})

        elif action == "login":
            # Authenticate looks for matching credentials
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                n = random.choice(range(1,9))
               # The context dictionary maps the 'variable_name' used in HTML to the Python variable
                return render(request, 'image.html', {'img_uri': images[n]})
                
            else:
                messages.error(request, "USer Does not exixt Sign up")

    return render(request, 'index.html')