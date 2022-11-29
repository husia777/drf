from django.db import models


class Locations(models.Model):
    name = models.TextField()
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(null=True)
    username = models.TextField()
    password = models.TextField()
    role = models.TextField()
    age = models.IntegerField()
    location = models.ManyToManyField("Locations")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username


class Ads(models.Model):
    name = models.TextField()
    author = models.ForeignKey('Users', on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='logos/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
