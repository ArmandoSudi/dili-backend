from rest_framework import serializers
from .models import Post, AutoPost, FurniturePost, ElectronicPost, HousePost, LawnPost, JobAndServicePost
from .models import PhotoURL, MobilePost, PostSummary

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class MobilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePost
        fields = '__all__'

class AutoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoPost
        fields = '__all__'

class FurniturePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FurniturePost
        fields = '__all__'

class ElectronicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicPost
        fields = '__all__'

class HousePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePost
        fields = '__all__'

class LawnPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawnPost
        fields = '__all__'

class JobAndServicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAndServicePost
        fields = '__all__'

class PhotoURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoURL
        fields = '__all__'

class PostSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSummary
        fields = "__all__"
