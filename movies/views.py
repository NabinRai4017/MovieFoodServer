from .models import Movie
from .serializers import MovieSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import (IsAuthenticated)


class MovieCreate(APIView):

    permission_classes = [IsAuthenticated]

    """
    create a new food.
    """
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieList(APIView):

    permission_classes = [IsAuthenticated]
    """
    List all foods
    """
    def get_object(self):
        try:
            return Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        serializer = MovieSerializer(many=True)
        response = {
            "error_code": 0,
            "message": "success",
            "data": serializer.data
        }
        return Response(response)

class MovieProcess(APIView):

    """
    update or delete a food instance.
    """
    def get_object(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        food = self.get_object(pk)
        serializer = MovieSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        food = self.get_object(pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MovieDetail(APIView):

    permission_classes = [IsAuthenticated]
    """
    Retrieve a food instance.
    """
    def get_object(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        food = self.get_object(pk)
        serializer = MovieSerializer(food)
        return Response(serializer.data)
