from django.conf import settings
from django.db import models


class Account(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    rasm=models.URLField(blank=True)
    obunachilari=models.ManyToManyField(settings.ACCOUNT,related_name='acc_obunachilari',blank=True)
    obunalar=models.ManyToManyField(settings.ACCOUNT,related_name='acc_obunalar',blank=True)

    def obunachilari_soni(self):
        return self.obunachilari.count()

    def obunalar_soni(self):
        return self.obunalar.count()