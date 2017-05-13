"""holyhappy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from newsongy import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.RootView.as_view(), name='root'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^goal/$', views.GoalView.as_view(), name='goal'),
    url(r'^pray/$', views.PrayView.as_view(), name='pray'),
    url(r'^update_attendance', views.AttendanceEditView.as_view(), name='update_attendance'),
    url(r'^bible_objective/$', views.BibleObjectiveView.as_view(), name='bible_objective'),
    url(r'^set_objective/(?P<page>\d+)$', views.SetObjectiveView.as_view(), name='set_objective'),
    url(r'^read_bible/$', views.ReadBibleView.as_view(), name='read_bible'),
    url(r'^update_read_bible', views.ReadBibleEditView.as_view(), name='update_read_bible'),
    url(r'^update_memo', views.MemoEditView.as_view(), name='update_memo'),

]
