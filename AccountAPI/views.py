from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status

@api_view(['POST'])
def loginPost(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({"status": False, "data": serializer.errors})
    user_obj = authenticate(username=serializer.data['username'], password=serializer.data['password'])
    if user_obj:
        return Response({"status": True, "data": {'token': str(Token.objects.get_or_create(user=user_obj)[0].key)}})
    return Response({"status": False, "message": "Invalid Credentials"})

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": True,
                "message": "User Created Successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": False,
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
