from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Style, Learner, Date, Registration, Course, Year


admin.site.register(Style)
admin.site.register(Learner)
admin.site.register(Date)
admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(Year)
