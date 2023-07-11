from django.urls import path, include

from .api_views import WomenModelViewSet

from rest_framework import routers

app_name = 'receiver'

router = routers.DefaultRouter()
router.register(r'women', WomenModelViewSet, basename='OMG')
print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]
