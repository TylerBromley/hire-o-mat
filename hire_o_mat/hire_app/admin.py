from django.contrib import admin

from .models import *

admin.site.register(UserProfile)

admin.site.register(CompanyProfile)

admin.site.register(Skill)

admin.site.register(City)

admin.site.register(Position)

admin.site.register(Message)
