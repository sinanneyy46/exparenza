from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryImageViewSet, ResultViewSet, HeadlineViewSet

router = DefaultRouter()
router.register('results', ResultViewSet)
router.register('gallery', GalleryImageViewSet)
router.register('headlines', HeadlineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
