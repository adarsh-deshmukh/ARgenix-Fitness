from django.contrib import admin
from .models import MyUser
from .models import Membership

# Register your models here.

class membershipAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","email","contact","Address","gender","weight","height","goal"]

admin.site.register(Membership,membershipAdmin)

class MyUserAdmin(admin.ModelAdmin):
    list_display=["Admin","Member","username","first_name","last_name","email"]

admin.site.register(MyUser,MyUserAdmin)