from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from notes.models import Note
from notes.api.serializers import NoteSerializer


class NoteViewSet(ModelViewSet):
    # To access the view the user must be authenticated
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    # Sort notes by most recent date
    ordering = ['-created_at']

    def get_queryset(self):
        # Verify that the user is authenticated and filter the notes created
        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user)
        # If not authenticated, returns the empty object
        else:
            return Note.objects.none()
        
    
    