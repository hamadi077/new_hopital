from django.shortcuts import render

# Create your views here.


from tokenize import Special
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User , Group
from django.contrib.auth import login, authenticate , logout
# from .formulaire import PatientForm
# Create your views here.


def home(request):
    template = "index.html"
    if request.user.is_authenticated:
        template = "patienthome.html"
    return render(request,template)
   

def about(request):
    return render(request,'about.html')  

def createaccountpage(request):
    context= {'erreur':''}
    print('logo')
    if request.method == 'POST' :
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        motdepasse = request.POST['password1']
        motdepasse2 = request.POST['password2']
        tel = request.POST['tele']
        gendre = request.POST['Gender'] 
        adress = request.POST['Address']
        date_naissance = request.POST['date']
        typedesang = request.POST['type']
        print(gendre)
        print(nom)
        print(email)

        if motdepasse != motdepasse2:
            context['erreur'] = 'password'
        else:
            user = User.objects.create_user(email,email,motdepasse)
            user.save()
            g =Group.objects.get(name='patient')      
            g.user_set.add(user)
            
            p = Patient.objects.create(gendre=gendre ,adresse = adress ,date_naissance= date_naissance,typeSang =typedesang,user=user,nom=nom,prenom=prenom, numtele= tel)
            p.save()

            return  redirect('/login')

    return render(request , 'createaccount.html',context)
    
    
def loginpage(request):
    message = ''
    if request.method == 'POST' :
        u = request.POST['nom']
        p = request.POST['password']
        user = authenticate(request , username=u, password=p ) 

        if user is not None :
            message = ''
            login(request , user)
            if user.is_superuser:
                return redirect ('/admin_home')
            else:
                return redirect ('/')
        else:
            message = 'erreur'
            

    return render(request ,'login.html',{'message':message})
    


def logoutt(request):
    logout(request)
    return redirect ('/login')

def patientprofile(request):
    p=request.user.patient
    context = {
        "p": p
    }
    return render(request, 'pateintprofile.html',context)


def doctorprofile(request):
    d=request.user.medecin
    context = {
        "d": d
    }
    return render(request, 'doctorprofile.html',context)

def make_apointement(r):
    p= r.user.patient
    tel = p.numtele
    if(r.method == 'POST'):
        tel = r.POST['tel']
        sym = r.POST['Symptoms']
        c= Consultation.objects.create(tel= tel,patient= p,symtoms=sym)
        c.save()
        print('saved')
        return redirect('/')

    return render(r,'pateintmakeappointments.html',{'tel':tel})



def AdminHome(request):
	
	return render(request,'adminhome.html')



def add_doctor(request):
    types = specialite.objects.all()
    context= {'erreur':'','types':types}

    if request.method == 'POST':
       if request.user.is_superuser :
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            email = request.POST['email']
            motdepasse = request.POST['password1']
            motdepasse2 = request.POST['password2']
            tel = request.POST['tele']
            date_naissance = request.POST['date']
            gendre = request.POST['gendre'] 
            adress = request.POST['Address']
            pk_specialite = request.POST['specialite']
            s = specialite.objects.get(pk =pk_specialite )

            if motdepasse != motdepasse2:
                context['erreur'] = 'password'
            
            else:
                user = User.objects.create_user( email, email=email, password=motdepasse)
                user.save()
                p = Medecin.objects.create(prenom= prenom ,gendre=gendre ,adresse = adress ,date_naissance= date_naissance ,user=user,numtele =tel,nom = nom,specialite=s )
                p.save()
                g =Group.objects.get(name='medecin')      
                g.user_set.add(user)
                return redirect('/admin_home')
           
    return render(request , 'adminadddoctor.html',context)


def adminviewDoctor(request):
	if not request.user.is_superuser:
		return redirect('login_admin')
	docs = Medecin.objects.all()
	d = { 'docs' : docs }
	return render(request,'adminviewDoctors.html',d)
