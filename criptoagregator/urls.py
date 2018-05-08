from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include('accounts.urls')),
    path("admin/", admin.site.urls),
    path('cry/', include('cryptoagregator.urls')),
]