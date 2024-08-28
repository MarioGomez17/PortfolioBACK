from rest_framework import viewsets, generics
from ...Models.ProjectModel import ProjectModel
from ...Serializers.ProjectSerializer import ProjectSerializer


class ProjectGetView(generics.RetrieveAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
