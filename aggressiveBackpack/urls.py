
from django.conf.urls import patterns, include, url
from django.contrib import admin
from aggressiveBackpack import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dim3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name="index"),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^settings/', views.settings, name='settings'),
    url(r'^login/', views.login, name='login'),
	url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^new-project/', views.new_project, name='new-project'),
)
