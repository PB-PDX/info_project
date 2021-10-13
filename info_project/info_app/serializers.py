from rest_framework import serializers 
from .models import Feeds, Snippets
from users.models import Profile
 
class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeds
        fields = ('__all__')

class SnipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')