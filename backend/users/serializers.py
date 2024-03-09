from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_compare = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password_compare"]
        extra_kwargs = {"email": {"required": True}}

    def validate(self, attrs):
        if attrs["password"] != attrs["password_compare"]:
            raise serializers.ValidationError("Password didn't match")
        return attrs
