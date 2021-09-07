from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=True)
    class Meta:
        model = UserProfile
        fields = ['user', 'first_name', 'last_name', 
                  'image', 'fb_profile', 'twitter_profile',
                  'linkedin_profile', 'website'
        ]