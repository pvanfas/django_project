from django.contrib import admin

from .models import Recruiter
from core.custom_admin import CustomAdmin


@admin.register(Recruiter)
class Recruiter(CustomAdmin):
    pass
