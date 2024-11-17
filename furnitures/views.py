from django.http import HttpResponse
from django.template import loader
from .models import Furniture
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages

def furnitures(request):
  myfurnitures = Furniture.objects.all().values()
  template = loader.get_template('all_products.html')
  context = {
    'myfurnitures': myfurnitures,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  myfurniture = Furniture.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'myfurniture': myfurniture,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))



#login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('recipes')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")

#register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")

#logout function
def custom_logout(request):
    logout(request)
    return redirect('login') 