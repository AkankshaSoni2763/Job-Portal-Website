from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from hr.models import Hr
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if Hr.objects.filter(user=user).exists():
                return redirect('hrdash')
            return redirect('dash')
        else:
            msg = "InValid Username or Password"
            return render(request,'authuser/login.html',{'msg':msg})
    return render(request,'authuser/login.html')


def candidateregister(request):
    return render(request,'authuser/candidateregister.html')

def hrregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/hrregister.html',{'msg':msg})
        user = User.objects.create_user(username=username, email=email, password=password)
        Hr(user=user).save()
        login(request, user) 
        return redirect('hrdash') 

    return render(request,'authuser/hrregister.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword') 
        if password != cpassword:
            msg = "Password did't match"
            return render(request,'authuser/candidateregister.html',{'msg':msg})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        
        login(request, user) 
        return redirect('dash')
    return render(request,'authuser/candidateregister.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
     
    return render(request, 'authuser/index.html')

def about(request):
    return render(request, 'authuser/about.html')



def contact(request):
    return render(request, 'authuser/contact.html')

def contact_submit(request):
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Here, you can process the form data as needed
        
        # Add a success message
        messages.success(request, 'Your message has been submitted successfully!')
        
        # Here, you can process the form data as needed
        
        # For demonstration, let's just redirect back to the contact page with a success message
        return HttpResponseRedirect('/contact/?success=true')
    else:
        # Handle GET requests if needed
        return render(request, 'contact_form.html')


