from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)



urlpatterns = [
    path('', include(router.urls)),
]
