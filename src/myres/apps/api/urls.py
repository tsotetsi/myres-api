from rest_framework import routers
from django.conf.urls import include, url
from bo_drf.routers import FlexiRouter

from myres.apps.api.views import LoginView

router = FlexiRouter()
router.add(r'^login/$', LoginView.as_view(), name='login')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]
