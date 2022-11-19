from django.contrib import admin
from . import models
# Register your models here.



@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title","parent","is_active"]
    list_filter = ["is_active","parent"]
    search_fields = ["title"]




class FileAdmin(admin.StackedInline):
    model = models.File
    fields = ["title","file","is_active"]
    extra=0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","is_active"]
    list_filter = ["is_active","created"]
    list_filter = ["title"]
    filter_horizontal = ["category"]
    inlines = [FileAdmin]