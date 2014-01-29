from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from dim3app import views
from django.conf import settings

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

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
