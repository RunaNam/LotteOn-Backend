from django.urls import path

from . import views

urlpatterns = [
    path('allergy/', views.AllergyList.as_view()),
    path('allergy/update/<int:pk>/', views.AllergyUpdate.as_view()),
    path('etc/', views.EtcList.as_view()),
]
