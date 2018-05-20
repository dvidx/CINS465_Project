from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.Survey_Model)
admin.site.register(models.Event_Model)
admin.site.register(models.Ticket_Model)
admin.site.register(models.Profil_Model)
admin.site.register(models.Chatline_Model)
