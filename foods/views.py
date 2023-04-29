from .models import Food
from .serializers import FoodSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import (IsAuthenticated)

class FoodCreate(APIView):

    permission_classes = [IsAuthenticated]

    """
    create a new food.
    """
    def post(self, request, format=None):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodList(APIView):

    permission_classes = [IsAuthenticated]
    """
    List all foods
    """
    def get_object(self):
        try:
            return Food.objects.all()
        except Food.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        serializer = FoodSerializer(many=True)
        response = {
            "error_code": 0,
            "message": "success",
            "data": serializer.data
        }
        return Response(response)

class FoodProcess(APIView):

    """
    update or delete a food instance.
    """
    def get_object(self,pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        food = self.get_object(pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        food = self.get_object(pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FoodDetail(APIView):

    permission_classes = [IsAuthenticated]
    """
    Retrieve a food instance.
    """
    def get_object(self,pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        food = self.get_object(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

