from rest_framework import viewsets, generics
from ...Models.ProgrammingLanguageModel import ProgrammingLanguageModel
from ...Serializers.ProgrammingLanguageSerializer import ProgrammingLanguageSerializer


class ProgrammingLanguageCreateView(generics.CreateAPIView):
    queryset = ProgrammingLanguageModel.objects.all()
    serializer_class = ProgrammingLanguageSerializer