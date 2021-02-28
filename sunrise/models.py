from django.db import models
from django.db.models import Model


class Categories(Model):
    name = models.CharField(verbose_name="Название категории", max_length=255)

    def __str__(self):
        return self.name


class Products(Model):
    name = models.CharField(verbose_name="Наименование товара", max_length=255)
    created_date = models.DateField(verbose_name="Дата создания", null=True, blank=True, auto_now_add=True)
    category = models.ForeignKey(Categories, verbose_name="Категория", on_delete=models.CASCADE)
    short_description = models.CharField(verbose_name="Краткое описание", max_length=255)
    img = models.ImageField(verbose_name="Иконка", null=True, blank=True, upload_to="sunrise")

    def __str__(self):
        return self.name
