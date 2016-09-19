# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User 
from django.utils.translation import ugettext_lazy as _ 

class Pacient(models.Model): 
    MG = 1
    MMOL = 2

    PA = 1
    DR = 2
    AP = 3

    ALEGERE_UNITATE_MASURA = (
            (MG, _('mg/dL')),
            (MMOL, _('mmol/L')),
            )

    CATEGORIE_UTILIZATOR = (
            (PA, _('Pacient')),
            (DR, _('Doctor')),
            (AP, _('Apartinator')),
            )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unitate_masura = models.SmallIntegerField(choices = ALEGERE_UNITATE_MASURA, default=MG) #conversia?
    valoare_max = models.SmallIntegerField(default = 90)
    valoare_min = models.SmallIntegerField(default = 60)
    #de definit culori min/max/normal
    #emailu e în useru de la django
    perioada_raportare = models.DurationField() #interval pă postgres
    categorie = models.SmallIntegerField(choices = CATEGORIE_UTILIZATOR, default = PA)
    telefon = models.CharField(#SMS auth?
            max_length=13)



# Create your models here.
