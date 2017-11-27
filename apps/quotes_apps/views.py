# Create your views here.

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import re

def index(request):
    return render(request, 'quotes_apps/index.html')
   
def login(request): 
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    # messages.success(request, "Successfully registered!")
    return redirect('/quotes')
    
def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    user = User.objects.get(email = result.email)
    return redirect('/quotes')

def quotes(request):
        # if validate_login(request.post_data):
    context ={
        'current_user':User.objects.get(id=request.session['user_id']),
        #'others':User.objects.exclude(id=request.session['user_id']),
        #'quotes':User.objects.get(id=request.session['user_id']).quotes.all()
    }
        
    return render(request, 'quotes_apps/quotes.html', context)
        #     return redirect('/')
    
def profile(request, id):
    profile = User.objects.get(id=id)
    context = {
        'user' : profile
    }
    return render(request, 'quotes_apps/profile.html', context)

def add_friend(request, id):
    User.objects.addFriend(id, request.session['user_id'])
  
    return redirect('/friends')


def remove_friend(request,id):
    User.objects.removeFriend(request.session['user_id'], id)
    return redirect('/friends')

def logout(request):
    request.session.clear()
    return redirect('/')
    


    

  







    




