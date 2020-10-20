from django.urls import path

from . import views

urlpatterns = [
    path('allergy/', views.AllergyList.as_view()),
    path('etc/', views.EtcList.as_view()),

]