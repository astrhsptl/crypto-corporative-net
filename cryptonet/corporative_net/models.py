from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Posts(models.Model):
    '''this model creating posts'''
    title = models.CharField(max_length=255, verbose_name='title')
    discription = models.TextField(max_length=511, verbose_name='discription')

    def get_absolute_url(self):
        return reverse_lazy('posts', kwargs={'id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'

class Orders(models.Model):
    STATUS = (
        ('passed', ('passed')),
        ('failed', ('failed')),
        ('not ready', ('not ready')),
        ('taked', ('taked'))
    )

    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=511)
    executor_id = models.ForeignKey(
        'Workers', on_delete=models.PROTECT, verbose_name='executor_id', blank=True
    )
    client_id = models.ForeignKey(
        'Clients', on_delete=models.PROTECT, verbose_name='client_id', blank=True
    )
    client_sum = models.IntegerField(default=0, verbose_name='client_sum')
    status = models.CharField(
        max_length=64,
        choices=STATUS,
        default='not ready',
    )
    create_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse_lazy('orders', kwargs={'id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'orders'


class Workers(models.Model):
    post_id = models.ForeignKey(
        Posts, null=True, on_delete=models.PROTECT, verbose_name='post_id', blank=True
    )
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse_lazy('workers', kwargs={'id': self.pk})

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    lastname = models.CharField(max_length=255, verbose_name='lastname')
    phone = models.CharField(max_length=64, verbose_name='phone')
    email = models.EmailField(verbose_name='email')

    def get_absolute_url(self):
        return reverse_lazy('clients', kwargs={'id': self.pk})

    def __str__(self):
        return self.name