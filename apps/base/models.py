from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название сайта")
    descriptions = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to="logo/")
    phone = models.CharField(max_length=255,verbose_name="Телефонный номер")
    email = models.EmailField(verbose_name="Электронная почта")
    locate = models.CharField(max_length=255,verbose_name="Адрес")
    locate_url = models.URLField(verbose_name="Ссылка в 2гис")

    def __str__(self):
        return self.descriptions

    class Meta:
        verbose_name = "Основная настройка"
        verbose_name_plural = "Основные настройки"

