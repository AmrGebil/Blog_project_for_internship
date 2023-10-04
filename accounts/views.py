# from django.contrib.auth import get_user_model
# from rest_framework import status
# from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
#
# from .serializers import AccountSerializer,UserLoginSerializer,UserRegisterationSerializer,ProfileSerializer,ProfileAvatarSerializer
# from .models import Profile
#
# User = get_user_model()
#
#
# class UserRegisterationAPIView(GenericAPIView):
#     """
#     An endpoint for the client to create a new User.
#     """
#
#     permission_classes = (AllowAny,)
#     serializer_class = UserRegisterationSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token = RefreshToken.for_user(user)
#         data = serializer.data
#         data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
#         return Response(data, status=status.HTTP_201_CREATED)
#
#
# class UserLoginAPIView(GenericAPIView):
#     """
#     An endpoint to authenticate existing users using their email and password.
#     """
#
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         serializer = AccountSerializer(user)
#         token = RefreshToken.for_user(user)
#         data = serializer.data
#         data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
#         return Response(data, status=status.HTTP_200_OK)
#
#
# class UserLogoutAPIView(GenericAPIView):
#     """
#     An endpoint to logout users.
#     """
#
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         try:
#             refresh_token = request.data["refresh"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserAPIView(RetrieveUpdateAPIView):
#     """
#     Get, Update user information
#     """
#
#     permission_classes = (IsAuthenticated,)
#     serializer_class = AccountSerializer
#
#     def get_object(self):
#         return self.request.user
#
#
# class UserProfileAPIView(RetrieveUpdateAPIView):
#     """
#     Get, Update user profile
#     """
#
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return self.request.user.profile
#
# class UserAvatarAPIView(RetrieveUpdateAPIView):
#     """
#     Get, Update user avatar
#     """
#
#     queryset = Profile.objects.all()
#     serializer_class = ProfileAvatarSerializer
#     permission_classes = (IsAuthenticated,)
#
#     def get_object(self):
#         return self.request.user.profile


from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from .serializers import AccountRegisterationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def register_Account(request):
    if request.method == 'POST':
        serializer = AccountRegisterationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def account_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        # Check if an email and password are provided
        if not email or not password:
            return Response({'error': 'Both email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Authenticate the user using email and password
        user = authenticate(request, username=email, password=password)

        if user:
            # Generate or retrieve an authentication token for the authenticated user
            token, _ = Token.objects.get_or_create(user=user)

            # Return the token in the response
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def account_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)