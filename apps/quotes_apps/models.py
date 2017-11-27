# Create your models here.

from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


class UserManager(models.Manager):

    def validate_login(self,post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self,post_data):
        errors = []
        print post_data['email']
        if not EMAIL_REGEX.match(post_data['email']):
            errors.append("invalid email")

        if len(post_data['name']) < 2:
            errors.append('Name too short')
        
        if len(post_data['alias']) < 2:
            errors.append('alias too short')

        if post_data['birthday'] == '':
           errors['birthday']= 'unable to register : user Ought to be over years of age'
    
        if errors:
            return {'errors':errors}

        newpassword = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
      
        return  User.objects.create(
                    name = post_data['name'],
                    alias = post_data['alias'],
                    email = post_data['email'],
                    password = newpassword,
                    birthday = post_data['birthday']
                )   
                
    def addFriend(self,friend_id,user_id):
      
        friend = User.objects.get(id = friend_id)
        
        
        user = User.objects.get(id =user_id)
        print user
       
        user.friends.add(friend)

        return user
       

    def removeFriend(self,friend_id, user_id):
       
        friend = self.get(id = friend_id)
        user = self.get(id =user_id)
        user.friends.remove(friend)
        return user

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.EmailField()
    birthday =models.DateField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    

class Quote(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_quotes")
    liked_by = models.ManyToManyField(User, related_name="liked_quotes")

        





















           




   
            
   
            



