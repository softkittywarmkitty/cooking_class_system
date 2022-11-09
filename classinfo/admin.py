from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Style, Learner, Registration, Course, Year, Month, Day, Availability


admin.site.register(Style)
admin.site.register(Learner)
admin.site.register(Registration)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(Month)
admin.site.register(Day)
admin.site.register(Availability)
