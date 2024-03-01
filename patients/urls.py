# patients/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^patients/$', views.PatientViewSet.as_view({'get': 'list', 'post': 'create'}), name='patients-list-create'),

    url(r'^patients/(?P<pk>\d+)/$', views.PatientViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='patient-detail'),
]
