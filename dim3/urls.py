from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from dim3app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dim3.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', views.index, name='index'),
	url(r'^about/', views.about, name='about'),
	url(r'^create/', views.create, name='create'),
	url(r'^plist/', views.plist, name='plist')
)
