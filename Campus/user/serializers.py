from .models import Users
from rest_framework import serializers

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # fields 指明为模型类的哪些字段被序列化


