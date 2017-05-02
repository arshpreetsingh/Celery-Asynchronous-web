from django.conf.urls import include, url
from django.contrib import admin

from feedback.views import upload_file

urlpatterns = [
    url(r'^feedback/$',upload_file, name="feedback"),
    url(r'^admin/', include(admin.site.urls)),
]
