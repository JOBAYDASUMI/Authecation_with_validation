from django.db import models
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]

    user_type=models.CharField(choices=USER,max_length=10)
    
    

    language_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.language_name}" 
    