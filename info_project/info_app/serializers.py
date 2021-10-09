from rest_framework import serializers 
from .models import FederalRegister
from users.models import Profile
 
class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalRegister
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')