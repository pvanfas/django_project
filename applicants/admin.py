from django.contrib import admin

from .models import Applicant
from .models import JobApplication
from core.custom_admin import CustomAdmin

# Register your models here.


@admin.register(JobApplication)
class JobApplication(CustomAdmin):
    pass


@admin.register(Applicant)
class ApplicantAdmin(CustomAdmin):
    pass
