from rest_framework.serializers import ModelSerializer
from notes.models import Note
from users.api.serializers import UserInfoSerializer


class NoteSerializer(ModelSerializer):
    # Get serialized fields from User model
    user = UserInfoSerializer()

    class Meta:
        model = Note
        # Data to be serialized
        fields = ['id', 'content', 'created_at', 'user']