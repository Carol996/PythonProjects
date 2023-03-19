from django.db import models


# creates universityCampus class
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=20, blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    # sets title display
    class Meta:
        verbose_name_plural = "University Campus"
