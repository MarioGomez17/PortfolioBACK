from rest_framework import generics
from ...Models.ProgrammingLanguageModel import ProgrammingLanguageModel
from ...Serializers.ProgrammingLanguageSerializer import ProgrammingLanguageSerializer


class ProgrammingLanguageDeleteView(generics.DestroyAPIView):
    queryset = ProgrammingLanguageModel.objects.all()
    serializer_class = ProgrammingLanguageSerializer