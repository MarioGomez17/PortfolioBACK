from rest_framework import viewsets, generics
from ...Models.DepartmentModel import DepartmentModel
from ...Serializers.DepartmentSerializer import DepartmentSerializer


class DepartmentDeleteView(generics.DestroyAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer