from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Sewa(models.Model):
    nama_pemesan = models.CharField(max_length=240, null=True,blank=False)
    no_ktp = models.IntegerField
    alamat = models.CharField(max_length=100, null=True,blank=False)
    intstalasi = models.CharField(max_length=100, null=True,blank=False)
    jabatan = models.CharField(max_length=100, null=True,blank=False)
    no_hp = models.IntegerField(null=True,blank=False)


def __str__(self):
    return self.nama_pemesan



