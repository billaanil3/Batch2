from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import exceptions
from rest_framework import serializers

from .models import Question


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "url",
        )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = "__all__"
        fields = (
            "id",
            "title",
            "status",
            "created_by"
        )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get("username", "")
        password = attrs.get("password", "")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    attrs['user'] = user
                else:
                    msg = "user id Deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Unable to login with this credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Must provide username and password"
            raise exceptions.ValidationError(msg)
        return attrs
