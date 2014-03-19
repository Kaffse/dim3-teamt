from django.conf.urls import patterns, include, url
from django.contrib import admin
from aggressiveBackpack import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^dashboard/', views.dashboard, name='dashboard'),
                       url(r'^settings/', views.settings, name='settings'),
                       url(r'^login/', views.user_login, name='login'),
                       url(r'^logout/', views.user_logout, name='logout'),
                       url(r'^register/', views.register, name='register'),
                       url(r'^new_project/', views.new_project, name='new_project'),
                       url(r'^project/(?P<project_name_url>\w+)/$', views.project, name='project'),
                       url(r'^user/', views.user, name='user'),
					   url(r'^getUsers/', views.getUsers, name='getUsers'),
)
