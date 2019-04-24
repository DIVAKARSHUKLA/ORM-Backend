from rest_framework import serializers
from .models import UserAnalysis, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


""" class UserRepliesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReplies
        fields = ('id', 'screen_name', 'name',
                  'postive', 'negative', 'neutral') """


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnalysis
        fields = ('id', 'screen_name', 'name', 'tweet_positive', 'tweet_negative', 'tweet_neutral', 'reply_positive', 'reply_negative',
                  'reply_neutral', 'follow_count', 'status_count', 'desc', 'profile_url', 'image_url', 'retweet_count', 'fav_count')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'image', 'mobile',
                  'address', 'company', 'party', 'dob')
