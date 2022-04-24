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
    client_sum = models.IntegerField(default=0, verbose_name='client_sum')
    status = models.CharField(
        max_length=64,
        choices=STATUS,
        default='not ready',
    )
    create_date = models.DateField(auto_created=True)

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
    active_order = models.ForeignKey(
        Orders, on_delete=models.PROTECT, verbose_name='active_order', blank=True
    )

    def get_absolute_url(self):
        return reverse_lazy('workers', kwargs={'id': self.pk})

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    order_id = models.ForeignKey(
        Orders, on_delete=models.PROTECT, verbose_name='order_id', blank=True
    )

    def get_absolute_url(self):
        return reverse_lazy('clients', kwargs={'id': self.pk})

    def __str__(self):
        return self.name