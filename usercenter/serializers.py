# _*_ coding: utf-8 _*_
# @Time     :   2020/9/21 18:00
# @Author       vanwhebin

from rest_framework import serializers
from usercenter.models import User
from django.contrib.auth.models import Group, Permission
# from rest_framework_jwt.serializers import JSONWebTokenSerializer


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission
		fields = '__all__'
