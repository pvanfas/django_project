from django.db import models
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField

from core.choices import NATIONALITY_CHOICES, PASSOUT_CHOICES, ROLE_CHOICES
from core.models import BaseModel, State


class Skill(BaseModel):
    name = models.CharField(max_length=128)
    about = models.TextField()
    skill = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("jobs:company_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("jobs:company_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("jobs:company_delete", kwargs={"pk": self.pk})

    def get_fields(self):
        return [
            (
                field.verbose_name.title(),
                field.value_from_object(self)
                if field.is_relation
                else field.value_from_object(self),
            )
            for field in self._meta.fields
        ]


class Job(BaseModel):
    job_title = models.CharField(max_length=128)
    job_post = models.CharField(max_length=128)
    job_category = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    job_requirment = models.CharField(max_length=128)
    salary = models.CharField(max_length=128)
    job_location = models.ForeignKey(
        State, related_name="applied_state", on_delete=models.CASCADE
    )
    job_description = models.TextField()

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return str(self.job_title)

    def get_absolute_url(self):
        return reverse_lazy("jobs:job_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("jobs:job_update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("jobs:job_delete", kwargs={"pk": self.pk})

    def get_fields(self):
        return [
            (
                field.verbose_name.title(),
                field.value_from_object(self)
                if field.is_relation
                else field.value_from_object(self),
            )
            for field in self._meta.fields
        ]
