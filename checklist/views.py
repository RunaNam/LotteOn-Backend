from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import UpdateAPIView

from .models import Allergy, Etc
from .serializers import AllergySerializer, EtcSerializer


class AllergyList(generics.ListCreateAPIView):
    queryset = Allergy.objects.all()
    serializer_class = AllergySerializer

#
# class AllergyUpdate(generics.ListCreateAPIView):
#     queryset = Allergy.objects.all()
#     serializer_class = AllergySerializer
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


class EtcList(generics.ListCreateAPIView):
    queryset = Etc.objects.all()
    serializer_class = EtcSerializer
