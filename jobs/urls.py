from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobOfferViewSet, RegionViewSet, IndustryViewSet


app_name = 'jobs'


router = DefaultRouter()
router.register('industries', IndustryViewSet)
router.register('regions', RegionViewSet)
router.register('jobs', JobOfferViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
