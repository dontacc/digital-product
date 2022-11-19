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
    file_set = FileSerializer(many=True)
    get_full_title = serializers.SerializerMethodField(method_name="title_id")

    class Meta:
        model = models.Product
        fields = ["id","title", "description", "avatar", "category", "file_set",
                  "get_full_title" ]  # liste file haram dar product mitonim bebinim

    def title_id(self, obj):
        return obj.title + " " + str(obj.id)
