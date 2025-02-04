from django.db import models
from django.db.models import SET_NULL


# Create your models here.

class Bolim(models.Model):
    nom = models.CharField(max_length=250)
    haqida = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Bo'limlar"


class Muallif(models.Model):
    ism = models.CharField(max_length=250)
    tirik = models.BooleanField(default=False)
    mamlakat = models.CharField(max_length=300, blank=True, null=True)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = "Mualliflar"


class Kitob(models.Model):
    nom = models.CharField(max_length=300)
    user = models.CharField(max_length=250)
    muallif = models.ForeignKey(Muallif, on_delete=SET_NULL, null=True)
    yil = models.DateField(blank=True, null=True)
    bolim = models.ForeignKey(Bolim, on_delete=SET_NULL, null=True)
    file = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Kitoblar"



