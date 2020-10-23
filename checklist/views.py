from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Allergy, Etc
from .serializers import AllergySerializer, EtcSerializer


# @api_view(['GET'])
class AllergyList(generics.ListAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


# @api_view(['POST'])
class AllergyUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer
    #
    # def update(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)



class EtcList(generics.ListCreateAPIView):
    queryset = Etc.objects.all()
    serializer_class = EtcSerializer
