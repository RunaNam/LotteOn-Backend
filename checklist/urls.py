from django.urls import path

from . import views

urlpatterns = [
    path('allergy/', views.AllergyList.as_view()),
    # path('allergy/update', views.AllergyUpdate.as_view()),
    path('etc/', views.EtcList.as_view()),

]