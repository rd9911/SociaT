from django.conf import settings
from rest_framework import serializers

from .models import Tweet

MAX_TWEET_CHAR = settings.MAX_TWEET_CHAR


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']
    
    def validate_content(self, value):
        if len(value) > MAX_TWEET_CHAR:
            raise serializers.ValidationError("You exceeded maximum number of characters (240)")
        return value