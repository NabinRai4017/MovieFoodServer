from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (MovieList, MovieDetail, MovieCreate, MovieProcess)

app_name = 'movies'

urlpatterns = [
    path('', MovieList.as_view()),
    # path('food/', MovieCreate.as_view()),
    path('<int:movie_id>/', MovieDetail.as_view()),
    # path('<int:movie_id>/<i', MovieProcess.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
