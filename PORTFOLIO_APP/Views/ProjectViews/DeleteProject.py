from rest_framework import generics
from ...Models.ProjectModel import ProjectModel
from ...Serializers.ProjectSerializer import ProjectSerializer


class ProjectDeleteView(generics.DestroyAPIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer