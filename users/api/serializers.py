from rest_framework.serializers import ModelSerializer
from users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        # Get password
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            # Password encryption
            instance.set_password(password)
        
        instance.save()
        return instance
    

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['id', 'email', 'username', 'first_name', 'last_name']


class UserUpdateInfoSerializer(ModelSerializer):
    class Meta:
        model = User
        # Data to be serialized
        fields = ['first_name', 'last_name']