from django.contrib import admin

from .models import Agent, Lead, User, Profile

admin.site.register(Agent)
admin.site.register(Lead)
admin.site.register(User)
admin.site.register(Profile)
