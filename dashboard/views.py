from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from dashboard.serializers import UserRegistrationSerializer,UserLoginSerializer,UserProfileSerializer, ItemAdditionSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User,Item
from django_filters.rest_framework import DjangoFilterBackend
from dashboard.filters import ItemFilter
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'login successful'},status=status.HTTP_200_OK)
            else:
                return Response({'msg': 'Invalid credentials'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

class UserRegistrationView(APIView):
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = get_tokens_for_user(user)
            
            return Response({'token':token,'msg':'Registration success'},status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class GetAllUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ItemAdditionView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = ItemAdditionSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'msg':'Addition success'},status=status.HTTP_201_CREATED)
        return Response({'error':'all fields are compulsory'},status=status.HTTP_400_BAD_REQUEST)


class ItemListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemAdditionSerializer
    queryset = Item.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ItemFilter
    search_fields = ['name', 'SKU', 'tags', 'category']
    ordering_fields = ['inStock', 'availableStock', 'created_at']

    def get(self, request, *args, **kwargs):
        if 'filter' in request.query_params:
            # Apply filters if 'filter' parameter is present
            return super().get(request, *args, **kwargs)
        else:
            # Retrieve all items if no filters are specified
            items = self.get_queryset()
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
        

