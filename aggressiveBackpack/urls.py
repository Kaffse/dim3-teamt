
from django.conf.urls import patterns, include, url
from django.contrib import admin
from aggressiveBackpack import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dim3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^create/', views.create, name='create'),
	url(r'^plist/', views.plist, name='plist'),
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.login, name='login'),
	url(r'^collaborate/', views.collaborate, name='collaborate'),
)
