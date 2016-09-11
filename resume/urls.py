from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^skills', SkillsView.as_view()),
    url(r'^studies', StudiesView.as_view())
]
