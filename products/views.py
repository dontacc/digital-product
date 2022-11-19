from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status





class ProductListView(APIView):
    def get(self,request):
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)