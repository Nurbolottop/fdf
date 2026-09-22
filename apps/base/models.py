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

class Banner(models.Model):
    title = models.CharField(max_length=255,verbose_name="Заголовоек")
    subtitle = models.CharField(max_length=255,verbose_name="Пол Заголовок")
    descriptions = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="banner_image", verbose_name="Фотография")

    def __str__(self):
            return self.title
    
    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class Numbers(models.Model):
     age = models.IntegerField(verbose_name="Лет в небе")
     naprav = models.IntegerField(verbose_name="Направлений")
     people = models.CharField(max_length=255,verbose_name="Пассажиров в год")
     rais = models.IntegerField(verbose_name="Рейсов в небе")

     class Meta:
        verbose_name = "Мы в числах"
        verbose_name_plural = "Мы в числах"