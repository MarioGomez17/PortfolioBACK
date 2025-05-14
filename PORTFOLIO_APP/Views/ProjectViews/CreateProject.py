from rest_framework import generics
from ...Models.ProjectModel import ProjectModel
from ...Serializers.ProjectSerializer import ProjectSerializer


class ProjectCreateView(generics.CreateAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer