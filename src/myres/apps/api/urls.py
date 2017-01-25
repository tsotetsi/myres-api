from django.conf.urls import include, url
from rest_framework import routers

from myres.apps.api.views import UserView, ResidenceView, StudentView, ApplicationView, FlatView


router = routers.DefaultRouter()
router.register(r'users', UserView, base_name='users')
router.register(r'residences', ResidenceView, base_name='residences')
router.register(r'students', StudentView, base_name='students')
router.register(r'applications', ApplicationView, base_name='applications')
router.register(r'flats', FlatView, base_name='flats')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
