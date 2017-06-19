# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Messages(models.Model):
    user_id = models.ForeignKey(Users)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    message_id = models.ForeignKey(Messages)
    user_id = models.ForeignKey(Users)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
