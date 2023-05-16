from django.shortcuts import render

from core.models import *
from django.views.generic import TemplateView
from common.mixins import StaffRequiredMixin

class DashboardIndex(StaffRequiredMixin, TemplateView):
    template_name = 'index.html'