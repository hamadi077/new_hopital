from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Medecin)
admin.site.register(Consultation)
admin.site.register(RandezVous)
admin.site.register(specialite)
