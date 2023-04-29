from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (FoodList, FoodDetail, FoodCreate, FoodProcess)

app_name = 'foods'

urlpatterns = [
    path('', FoodList.as_view()),
    # path('food/', FoodCreate.as_view()),
    path('<int:pk>/', FoodDetail.as_view()),
    # path('<int:pk>/', FoodProcess.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
