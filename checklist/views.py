from django.shortcuts import render
from rest_framework import generics
from .models import Allergy, Etc
from .serializers import AllergySerializer, EtcSerializer


class AllergyList(generics.ListCreateAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer


class EtcList(generics.ListCreateAPIView):
    queryset = Etc.objects.all()
    serializer_class = EtcSerializer
