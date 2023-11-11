from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes.api.views import NoteViewSet


router_notes = DefaultRouter()
router_notes.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('', include(router_notes.urls))
]
