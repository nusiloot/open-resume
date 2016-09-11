from django.views.generic import TemplateView
from django.shortcuts import render
from .models import *


class BaseView(TemplateView):
    person = IdentityModel.objects.first()

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        context['person'] = self.person
        context['has_studies'] = self.person.has_studies
        context['has_skills'] = self.person.has_skills

        return context

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class HomeView(BaseView):
    template_name = 'home.html'


class SkillsView(BaseView):
    template_name = 'skills.html'

    def __init__(self, **kwargs):
        super(SkillsView, self).__init__(**kwargs)
        self.skills = self.person.skills.all() if self.person else None

    def get_context_data(self, **kwargs):
        context = super(SkillsView, self).get_context_data(**kwargs)
        context['skills_categories'] = SkillsModel.get_categories(self.person)
        context['skills'] = self.skills
        return context


class StudiesView(BaseView):
    template_name = 'studies.html'

    def __init__(self, **kwargs):
        super(StudiesView, self).__init__(**kwargs)
        self.studies = self.person.studies.all() if self.person else None

    def get_context_data(self, **kwargs):
        context = super(StudiesView, self).get_context_data(**kwargs)
        context['studies'] = self.studies
        return context
