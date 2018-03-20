from django.db import models

# Create your models here.
class Survey_Model(models.Model):
    survey_name = models.CharField(max_length=120)
    survey_creation = models.DateField()
    survey_description = models.CharField(max_length=240)
    survey_size = models.IntegerField()

    def __str__(self):
        return "Survey " + str(self.id) + ": " + str(self.survey_name)
