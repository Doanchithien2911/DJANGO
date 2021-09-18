from django.contrib import admin
from .models import User,Todo
# Register your models here.

class DisplayUser(admin.ModelAdmin):
    list_display=["id","username","email","is_active"]

class DisplayToDo(admin.ModelAdmin):
    list_display=["id","title","description","user_id","date_complete","status","date_create","date_update"]



admin.site.register(User,DisplayUser)
admin.site.register(Todo,DisplayToDo)