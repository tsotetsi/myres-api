from django.conf.urls import include, url
from bo_drf.routers import FlexiRouter

from myres.apps.api.views import LoginView, UserProfileView

router = FlexiRouter()
router.add(r'^login/$', LoginView.as_view(), name='login')
router.register(r'user-profiles', UserProfileView, base_name='user-profiles')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),    
]
