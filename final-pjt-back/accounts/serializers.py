from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    like_genre1 = serializers.CharField(max_length=50)
    like_genre2 = serializers.CharField(max_length=50)
    like_genre3 = serializers.CharField(max_length=50)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['like_genre1'] = self.validated_data.get('like_genre1')
        data['like_genre2'] = self.validated_data.get('like_genre2')
        data['like_genre3'] = self.validated_data.get('like_genre3')
        return data

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'