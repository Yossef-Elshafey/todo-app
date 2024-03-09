from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import status

from users.serializers import UserSerializer


class SignUp(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            ser_data = serializer.data
            user = User.objects.create(
                username=ser_data["username"],
                email=ser_data["email"],
            )
            user.set_password(request.data["password"])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "id":user.pk})
        return Response(serializer.errors)


class Login(viewsets.ViewSet):
    def create(self, request):
        """
        404 email or password incorrect
        400 email or password was not provided
        500 both were not provided
        """
        try:
            email = request.data["email"]
            user = get_object_or_404(User, email=email)
            # password incorrect
            if not user.check_password(request.data["password"]):
                return Response(
                    {"detail": "Not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            token, created = Token.objects.get_or_create(user=user)
            return Response({"Token": token.key, "id": user.id})
        # either email or password were not provided
        except MultiValueDictKeyError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        # email incorrect *uses the default get_object_or_404 response*
        return Response({})


# still with logout ??!
