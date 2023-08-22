from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) # if we use auto_now_add=True we will never be able to edit date posted instead we 
    # we are using timezone utility using which even if user updates post they will see the time as time of update
    author = models.ForeignKey(User, on_delete=models.CASCADE) # we need to get the author details from the auth table hence import user above
    # its a one to many relationship a user can have multiple posts
    #in this app if user deletes then all his posts also delete read documentation
    
    def __str__(self) : # when you query the db then this dunder function will show the title generic name Post.object.all() will give Post: Blog 1 instead of Post : Post obeject 1
        return self.title   
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    