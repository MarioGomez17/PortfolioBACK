from rest_framework import viewsets, generics
from ...Models.DepartmentModel import DepartmentModel
from ...Serializers.DepartmentSerializer import DepartmentSerializer


class DepartmentsGetView(generics.ListAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer