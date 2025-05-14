from rest_framework import generics
from ...Models.RoleModel import RoleModel
from ...Serializers.RoleSerializer import RoleSerializer


class RoleDeleteView(generics.DestroyAPIView):
    queryset = RoleModel.objects.all()
    serializer_class = RoleSerializer