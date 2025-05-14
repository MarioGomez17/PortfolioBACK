from rest_framework import generics
from ...Models.ProjectModel import ProjectModel
from ...Serializers.ProjectSerializer import ProjectSerializer


class ProjectsGetView(generics.ListAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer
