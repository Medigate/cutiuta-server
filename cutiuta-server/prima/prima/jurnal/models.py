from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Pacient(models.Model):
    MG = 1
    MMOL = 2
    ALEGERE_UNITATE_MASURA = (
            (MG, _('mg/dL'))
            (MMOL, _('mmol/L')),
            )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unitate_masura = models.SmallIntegerField(choices = ALEGERE_UNITATE_MASURA, default=MG)
    valoare_max = models.SmallIntegerField(default = 90)
    valoare_min = models.SmallIntegerField(default = 60)
    #de definit culori min/max/normal
    #de implementat persoana de contact
    perioada_raportare = models.DurationField()


# Create your models here.
