from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	url(r'',include('food.urls')),
    url(r'^admin/', admin.site.urls),
]


urlpatterns += staticfiles_urlpatterns()
