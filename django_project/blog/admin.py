from django.contrib import admin
from . models import Post

admin.site.register(Post) # this is so that you can access the db from the admin site of you application
