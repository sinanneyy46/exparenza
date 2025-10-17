from rest_framework import serializers
from .models import Result
from .models import GalleryImage, Headline


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
        

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'


class HeadlineSerializer(serializers.ModelSerializer):
    short_content = serializers.ReadOnlyField()

    class Meta:
        model = Headline
        fields = '__all__'
