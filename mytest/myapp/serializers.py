from django.db.models import fields
from rest_framework import serializers
from .models import User,Todo


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255)
    re_password = serializers.CharField(max_length=255)

class GetUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
class ToDo(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    user_id = serializers.IntegerField()
    date_complete = serializers.DateField()
    status = serializers.CharField(max_length=20)


class GetToDo(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields=('id','title','description','user_id','date_complete','status')


