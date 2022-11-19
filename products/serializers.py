from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ["title", "description", "avatar"]


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ["title", "file"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = models.Product
        fields = ["title", "description", "avatar", "category"]
