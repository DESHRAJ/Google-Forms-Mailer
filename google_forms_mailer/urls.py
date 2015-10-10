from django.conf.urls import include, url
from django.contrib import admin
from mailer.views import mailer, home
urlpatterns = [
    # Examples:
    url(r'^$', 'mailer.views.home', name='home'),
    url(r'^mailer$', 'mailer.views.mailer', name='mailer'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
