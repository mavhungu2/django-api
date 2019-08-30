from django.db import models


class Currency(models.Model):

    name = models.CharField(max_length=50)
    value = models.FloatField()

    class Meta:
        db_table = "currencies"
