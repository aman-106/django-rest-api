from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('patients.urls')),  # Assuming your API endpoints are defined in patients.urls
]

