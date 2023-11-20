from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import CustomRegisterSerializer
from .models import User

# Create your views here.
@api_view(['GET'])
def user_detail(request):
    if request.method == 'GET':
        Users = get_list_or_404(User)
        serializer = CustomRegisterSerializer(Users, many=True)
        return Response(serializer.data)
        