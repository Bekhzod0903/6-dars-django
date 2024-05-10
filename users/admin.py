from django.contrib import admin
from .models import CustomUser
# Register your models here.



# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id','username','first_name','image')
#     list_filter = ('username','email','last_name')
#
# admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(CustomUser)
