from rest_framework import generics
from ...Models.DepartmentModel import DepartmentModel
from ...Serializers.DepartmentSerializer import DepartmentSerializer


class DepartmentCreateView(generics.CreateAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer