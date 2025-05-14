from rest_framework import generics
from ...Models.RoleModel import RoleModel
from ...Serializers.RoleSerializer import RoleSerializer


class RoleUpdateView(generics.UpdateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer
