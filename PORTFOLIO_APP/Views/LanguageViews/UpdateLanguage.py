from rest_framework import viewsets, generics
from ...Models.LanguageModel import LanguageModel
from ...Serializers.LanguageSerializer import LanguageSerializer


class LanguageUpdateView(generics.UpdateAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer