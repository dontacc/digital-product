from django.db import models
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    parent =  models.ForeignKey("self",on_delete=models.CASCADE,verbose_name="parent",blank=True,null=True )
    title = models.CharField(_("title"),max_length=50)
    description = models.TextField(_("description"),blank=True)
    avatar = models.ImageField(_("avatar"),blank=True , upload_to="categories")
    is_active = models.BooleanField(_("active"),default=True)


    def __str__(self):
        return self.title


    class Meta:
        db_table = "Categories"
        verbose_name = _("Category")
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_("avatar"), blank=True, upload_to="categories")
    is_active = models.BooleanField(_("active"), default=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = "producst"
        verbose_name = _("product")
        verbose_name_plural = "products"



class File(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    file = models.FileField(_("file") , upload_to="files")
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

    class Meta:
        db_table = _("files")
        verbose_name = "file"
        verbose_name_plural = "files"


