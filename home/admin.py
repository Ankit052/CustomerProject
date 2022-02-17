from django.contrib import admin
from .models import User,Customer

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name","last_name","email","mobile_no"] 

@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ["user","profile_number","created_on"] 