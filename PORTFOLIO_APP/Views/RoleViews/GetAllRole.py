from rest_framework import generics
from ...Models.RoleModel import RoleModel
from ...Serializers.RoleSerializer import RoleSerializer


class RolesGetView(generics.ListAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
