from rest_framework import serializers
from ..Models import RoleModel


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ['Id_Role', 'Name_Role']