from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from aggressiveBackpack import views
from django.conf import settings

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
    url(r'^new_project/', views.new_project, name='new_project'),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^$', views.index, name='index'),
	#url(r'^about/', views.about, name='about'),
	#url(r'^create/', views.create, name='create'),
	#url(r'^plist/', views.plist, name='plist'),
	#url(r'^register/', views.register, name='register'),
	#url(r'^login/', views.login, name='login'),
	#url(r'^collaborate/', views.collaborate, name='collaborate'),
	#url(r'^logout/$', views.user_logout, name='logout'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
