from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserInfoSerializer, UserRegisterSerializer, UserUpdateInfoSerializer


# User registration view
class RegisterUserView(APIView):
    def post(self, request):
        # In "request.data" there is all the user information
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # Save user
            serializer.save()
            # Send user data
            return Response(serializer.data)

        # In case of error, a status of type 400 is returned
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User information view
class UserInfoView(APIView):
    # Only authenticated users will be able to make this request.
    permission_classes = [IsAuthenticated]

    # Get serialized data
    def get(self, request):
        # We get data from the user serializer
        serializer = UserInfoSerializer(request.user)
        # Send user data
        return Response(serializer.data)
    
    # Update user data
    def put(self, request):
        # Get user ID
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateInfoSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            # Save changes
            serializer.save()
            # Send updated user data
            return Response(serializer.data)
            
        # In case of error, a status of type 400 is returned
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
