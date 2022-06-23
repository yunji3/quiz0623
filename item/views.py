from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category,Item
from item.serializers import CategorySerializer
# Create your views here.

class CategoryView(APIView):
    def get(self, request):

       return Response(CategorySerializer.data)


