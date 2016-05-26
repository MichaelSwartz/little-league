from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^roster/', include('roster.urls')),
    url(r'^admin/', admin.site.urls),
]