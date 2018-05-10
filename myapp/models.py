from django.db import models

from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Survey_Model(models.Model):
    survey_name = models.CharField(max_length=120)
    survey_creation = models.DateField()
    survey_description = models.CharField(max_length=240)
    survey_size = models.IntegerField()

    def __str__(self):
        return "Survey " + str(self.id) + ": " + str(self.survey_name)

class Event_Model(models.Model):
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=240)
    image = models.ImageField(
        upload_to='uploads/%Y/%m/%d/'
    )
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)

    def __str__(self):
        return "Event " + str(self.id) + ": " + str(self.name)

class Ticket_Model(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    event = models.OneToOneField(
        Event_Model,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    info = models.CharField(max_length=240)

    def __str__(self):
        return "Ticket " + str(self.id) + ": " + str(self.user)

class Bid_Model(models.Model):
    ticket = models.ForeignKey(
        Ticket_Model,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    bid = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "Bid " + str(self.id) + ": " + str(self.ticket)

class Profil_Model(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    creation=models.DateTimeField(auto_now_add=True, blank=True)
    picture=models.ImageField(
        upload_to=None,
        height_field=None,
        width_field=None
    )

class Chat_Model(models.Model):
    user1 = models.ForeignKey(
        User,
        null=True,
        related_name='user1',
        on_delete=models.CASCADE
    )
    user2 = models.ForeignKey(
        User,
        null=True,
        related_name='user2',
        on_delete=models.CASCADE
    )

class Chatline_Model(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    chat = models.ForeignKey(
        Chat_Model,
        on_delete=models.CASCADE
    )
    creation = models.DateTimeField(auto_now_add=True, blank=True)
    text = models.TextField()
