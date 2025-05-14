from rest_framework import generics
from ...Models.RoleModel import RoleModel
from ...Serializers.RoleSerializer import RoleSerializer


class RoleCreateView(generics.CreateAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer