from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    path("jobs/", login_required(views.JobListView.as_view()),
         name="job_list"),
    path("jobs/new/",
         login_required(views.JobCreateView.as_view()),
         name="job_new"),
    path(
        "jobs/<str:pk>/",
        login_required(views.JobDetailView.as_view()),
        name="job_detail",
    ),
    path(
        "jobs/update/<str:pk>/",
        login_required(views.JobUpdateView.as_view()),
        name="job_update",
    ),
    path(
        "jobs/delete/<str:pk>/",
        login_required(views.JobDeleteView.as_view()),
        name="job_delete",
    ),
    # path('countries/', login_required(views.CountryListView.as_view()),name='country_list'),
    # path('countries/new/', login_required(views.CountryCreateView.as_view()),name='country_new'),
    # path('countries/<str:pk>/', login_required(views.CountryDetailView.as_view()),name='country_detail'),
    # path('countries/update/<str:pk>/', login_required(views.CountryUpdateView.as_view()),name='country_update'),
    # path('countries/delete/<str:pk>/', login_required(views.CountryDeleteView.as_view()),name='country_delete'),
    #
    # path('states/', login_required(views.StateListView.as_view()),name='state_list'),
    # path('states/new/', login_required(views.StateCreateView.as_view()),name='state_new'),
    # path('states/<str:pk>/', login_required(views.StateDetailView.as_view()),name='state_detail'),
    # path('states/update/<str:pk>/', login_required(views.StateUpdateView.as_view()),name='state_update'),
    # path('states/delete/<str:pk>/', login_required(views.StateDeleteView.as_view()),name='state_delete'),
    path("skills/",
         login_required(views.SkillListView.as_view()),
         name="skill_list"),
    path("skills/new/",
         login_required(views.SkillCreateView.as_view()),
         name="skill_new"),
    path(
        "skills/<str:pk>/",
        login_required(views.SkillDetailView.as_view()),
        name="skill_detail",
    ),
    path(
        "skills/update/<str:pk>/",
        login_required(views.SkillUpdateView.as_view()),
        name="skill_update",
    ),
    path(
        "skills/delete/<str:pk>/",
        login_required(views.SkillDeleteView.as_view()),
        name="skill_delete",
    ),
]
