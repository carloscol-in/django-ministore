from rest_framework.views import APIView
from rest_framework.response import Response

from app.users.models import User
from app.users.serializers import UserSerializer


class ListUsers(APIView):
    
    
    def get(self, request, format=None):
        """List all users.
        """
        users = [u for u in User.objects.all()]
        serialized_users = UserSerializer(users, many=True)
        return Response(serialized_users.data)