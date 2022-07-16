from django.db import models


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30, verbose_name='Наименование категории', db_index=True)
    slug = models.SlugField(max_length=30, verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class IceCream(models.Model):
    objects = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    views = models.PositiveIntegerField(verbose_name='Просмотры', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженые'
        ordering = ['-created_at', '-name']
