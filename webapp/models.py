from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ACTIVE = 'activ', 'activ'
    BLOCKED = 'blocked', 'blocked'


class Book(models.Model):
    author = models.CharField(max_length=100,
                              null=False,
                              blank=False,
                              verbose_name='Author')
    email = models.EmailField(max_length=100,
                              null=False, blank=False,
                              verbose_name='Email')
    text = models.TextField(max_length=3000,
                            null=False, blank=False,
                            verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created date')
    updated_ad = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Updated date')
    status = models.TextField(verbose_name='Status',
                              choices=StatusChoices.choices,
                              max_length=100,
                              default=StatusChoices.ACTIVE)

    def __str__(self):
        return f'{self.author} {self.text} {self.email} {self.status}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

