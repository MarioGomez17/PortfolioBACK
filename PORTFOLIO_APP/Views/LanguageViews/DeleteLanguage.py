from rest_framework import generics
from ...Models.LanguageModel import LanguageModel
from ...Serializers.LanguageSerializer import LanguageSerializer


class LanguageDeleteView(generics.DestroyAPIView):
    queryset = LanguageModel.objects.all()
    serializer_class = LanguageSerializer