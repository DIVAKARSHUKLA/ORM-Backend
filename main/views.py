from .models import UserAnalysis, UserProfile
from main.utility import twarccus
from rest_framework import viewsets
from .serializers import UserSerializer, UserProfileSerializer

# Create your views here.


class UserView(viewsets.ModelViewSet):
    queryset = UserAnalysis.objects.all()
    serializer_class = UserSerializer


class UserProfile(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
