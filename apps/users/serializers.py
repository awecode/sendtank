from rest_framework import serializers

from .models import Role, Company, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')


class RoleSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    active = serializers.SerializerMethodField()

    def get_active(self, obj):
        return self.active.id == obj.id if self.active else False

    def __init__(self, *args, **kwargs):
        self.active = kwargs.pop('active', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Role
        fields = ('id', 'type', 'company', 'active')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email')
