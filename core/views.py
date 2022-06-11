import json

from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView

from core.models import Country
from core.models import District
from core.models import State


class Index(TemplateView):
    template_name = "app/index.html"


class StateListView(ListView):
    queryset = State.objects.filter(is_active=True)
    template_name = "app/pages/state_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_link"] = reverse_lazy("core:state_new")
        return context


class StateDetailView(DetailView):
    queryset = State.objects.filter(is_active=True)
    template_name = "app/common/object_detail.html"


class StateCreateView(CreateView):
    model = State
    template_name = "app/common/object_form.html"
    fields = "__all__"


class StateUpdateView(UpdateView):
    model = State
    template_name = "app/common/object_form.html"
    fields = "__all__"


class StateDeleteView(DeleteView):
    model = State
    template_name = "app/common/confirm_delete.html"
    success_url = reverse_lazy("core:state_list")


class CountryListView(ListView):
    queryset = Country.objects.filter(is_active=True)
    template_name = "app/pages/country_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_link"] = reverse_lazy("core:country_new")
        return context


class CountryDetailView(DetailView):
    queryset = Country.objects.filter(is_active=True)
    template_name = "app/common/object_detail.html"


class CountryCreateView(CreateView):
    model = Country
    template_name = "app/common/object_form.html"
    fields = "__all__"


class CountryUpdateView(UpdateView):
    model = Country
    template_name = "app/common/object_form.html"
    fields = "__all__"


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "app/common/confirm_delete.html"
    success_url = reverse_lazy("core:country_list")


class DistrictListView(ListView):
    queryset = District.objects.filter(is_active=True)
    template_name = "app/pages/district_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_link"] = reverse_lazy("core:district_new")
        return context


class DistrictDetailView(DetailView):
    queryset = District.objects.filter(is_active=True)
    template_name = "app/common/object_detail.html"


class DistrictCreateView(CreateView):
    model = District
    template_name = "app/common/object_form.html"
    fields = "__all__"


class DistrictUpdateView(UpdateView):
    model = District
    template_name = "app/common/object_form.html"
    fields = "__all__"


class DistrictDeleteView(DeleteView):
    model = District
    template_name = "app/common/confirm_delete.html"
    success_url = reverse_lazy("core:district_list")
