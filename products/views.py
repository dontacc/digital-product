from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers
from rest_framework import status


class ProductListView(APIView):
    def get(self, request):
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(products, many=True, context={"request": request})
        search_fields = ['title']
        return Response(serializer.data)



class ProductDetail(APIView):
    def get(self, request, pk):
        try :
            product = models.Product.objects.get(pk=pk)
        except product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ProductSerializer(product , context={"request":request})
        return Response(serializer.data)
