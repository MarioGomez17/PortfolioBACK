from rest_framework import generics
from ...Models.DepartmentModel import DepartmentModel
from ...Serializers.DepartmentSerializer import DepartmentSerializer


class DepartmentGetView(generics.RetrieveAPIView):
    queryset = DepartmentModel.objects.all()
    serializer_class = DepartmentSerializer
