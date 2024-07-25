from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Permission(models.Model):
    name = models.CharField(max_length=255, unique=True)