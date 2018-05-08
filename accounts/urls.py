from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^adduser/', views.UserCreate.as_view(), name='account-create'),
    url("", include('rest_framework.urls')),
]
