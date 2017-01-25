from django.conf.urls import include, url
from rest_framework import routers

from myres.apps.api.views import UserProfileView


router = routers.DefaultRouter()
router.register(r'user-profiles', UserProfileView, base_name='user-profiles')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
