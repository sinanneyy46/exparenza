from rest_framework import viewsets, filters
from .models import Result
from .serializers import ResultSerializer
from .models import GalleryImage, Headline
from .serializers import GalleryImageSerializer, HeadlineSerializer

class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.filter(published=True).order_by('id')

    def get_queryset(self):
        # Only return published results
        return Result.objects.filter(published=True).order_by('id')


class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']  # 👈 enable ?search=

    def get_queryset(self):
        return GalleryImage.objects.filter(published=True).order_by('-uploaded_at')


class HeadlineViewSet(viewsets.ModelViewSet):
    queryset = Headline.objects.all()
    serializer_class = HeadlineSerializer

    def get_queryset(self):
        return Headline.objects.filter(published=True).order_by('-created_at')