from django.contrib import admin
from .models import LikePost, Profile, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
