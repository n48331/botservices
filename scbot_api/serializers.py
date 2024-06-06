from rest_framework import serializers
from .models import Communication, File, Project

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communication
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    communications = CommunicationSerializer(many=True)
    files = FileSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_id', 'asset_name', 'asset_category', 'campaign_type', 'project_type', 'brand', 'country', 'csm', 'pmo', 'created_at', 'communications', 'files']


# class FoodSpotDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FoodSpot
#         fields = ('id', 'name', 'image', 'rating', 'time', 'location', 'categories', 'reel')