from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    # path("accounts/", include('accounts.urls')),
    path("api/", include('cryptoagregator.api.urls')),
    path("index/", include('cryptoagregator.vue.urls')),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]