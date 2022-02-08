

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


class Patient(models.Model):

    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20) 
    adresse = models.CharField(max_length=20)
    numtele = models.CharField(default="11111111",max_length=10)
    date_naissance = models.DateField(auto_now_add=True)
    typeSang = models.CharField(default= "A" ,max_length=5)
    gendre = models.CharField(default = "Masculin",max_length=7)
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.prenom+ " "+self.nom


class specialite(models.Model):
    specialite = models.CharField(max_length= 50)
    def __str__(self):
        return self.specialite

class Medecin(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    numtele = models.CharField(default="11111111",max_length=10)
    date_naissance = models.DateField(default= None)   
    gendre = models.CharField(default = "Male",max_length=7)    
    specialite = models.ForeignKey(specialite , on_delete=models.CASCADE,default=None)
    user= models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.prenom+ " "+self.nom


class Consultation(models.Model):
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE)  
    symtoms = models.CharField(max_length= 50,default=None)
    tel= models.CharField(max_length= 15)

class RandezVous(models.Model):
     medecin = models.ForeignKey(Medecin , on_delete=models.CASCADE)
     consultation = models.ForeignKey(Consultation , on_delete=models.CASCADE)
     date= models.DateField(default= None)
     description = models.CharField(max_length= 50)



      


