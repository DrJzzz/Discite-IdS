from django.urls import path
from .views import CardList, CardDetail

urlpatterns = [

    path('cards/', CardList.as_view(), name='card-list'),
    path('cards/<int:pk>/', CardDetail.as_view(), name='card-detail'),
]