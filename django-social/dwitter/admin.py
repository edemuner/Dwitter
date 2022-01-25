from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet
# Register your models here.

class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
     # only display the "username" field
    fields = ['username']
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# admin.site.register(Profile)
admin.site.register(Dweet)