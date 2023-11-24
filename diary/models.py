from accounts.models import CustomUser
from django.db import models


class Diary(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='User', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='Title', max_length=40)
    content = models.TextField(verbose_name='Content', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='Picture1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='Picture2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='Picture3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Upload date', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Update dates', auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'

    def __str__(self):
        return self.title

