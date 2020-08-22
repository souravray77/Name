from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .models import cv,data,mes,room,up
# Create your views here.

def home(request):
    if User.is_authenticated:

        if up.objects.filter(user=request.user).exists():
            upp = up.objects.get(user=request.user)
            upp.flag = 'False'
            upp.updating = 'False'
            upp.save()
        else:
            uppp = up(user=request.user,flag='False',updating='False')
            uppp.save()
    return render(request,'h.html')
def reg(request):
    if request.method == 'POST':
        firstname = request.POST['n1']
        lastname = request.POST['n2']
        email = request.POST['em']
        password1 = request.POST['p1']
        password2 = request.POST['p2']
        username = request.POST['un']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken ")
                return redirect("reg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken ")
                return redirect("reg")
            else:
                user = User.objects.create_user(password=password1,email=email,first_name=firstname,last_name=lastname,username=username)
                user.save()
                
                return redirect("/")
        
        
        else:
        
            messages.info(request,"password not matching")
            return redirect("reg")
    else:
        return render(request,'create.html')
def logi(request):
    if request.method == 'POST':
        username = request.POST['UN']
        password = request.POST['p']    
        username1=username
        password1=password
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        
            return redirect('/',)
        else:
            messages.info(request,"Somthing Wrong")
            return redirect("logi")    
    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def cvv(request):
    un = request.user
    print(un)
    roy = {}
    roy = cv.objects.filter(user=un).exists()
    if roy is True:
        yourcv = cv.objects.get(user=un)
        contaxt = {
            'fullname':yourcv.full_name,
            'fathername':yourcv.father_name,
            'cheak':roy,
            'name':un,
        }
    
    else:
        contaxt={
        'cheak':roy
        }
        
    return render(request,'cv.html',contaxt)
def ccv(request):
    if request.method=='POST':
        royii = request.POST["full_name"]
        fn = request.POST['fn']
        mn = request.POST['mn']
        na = request.POST['na']
        re = request.POST['re']
        db = request.POST['db']
        us = request.user
        cvs = cv(user=us,full_name=royii,father_name=fn,mother_name=mn,nationality=na,religion=re,date_of_birth=db)
        cvs.save()
        return redirect('/')
    else:
        return render(request,'ccv.html')

def mass(request):
    if request.method=='POST':

        cuser = request.user
        suser = request.POST["user_name"]
        if User.objects.filter(username=suser).exists():
            recever = User.objects.get(username=suser)
            sender = User.objects.get(username=cuser)
            reid = recever.id
            seid = sender.id
            roy = str(reid)+str(seid)
            nroy = str(seid)+str(reid)
            if mes.objects.filter(fuser=roy).exists():

                if data.objects.filter(fuserr=roy).exists():
                    if room.objects.filter(user=cuser).exists():
                        roy3 = room.objects.get(user=cuser)
                        roy3.croom = roy
                        roy3.save()
                    else:
                        roy4 = room(user=cuser,croom=roy)
                    
                        
                        roy4.save()
                    
                    messe = data.objects.filter(fuserr=roy)
                    
                    
                    contaxt = {
                        'messe':messe,
                        'paramiter':True,
                        'cuser':cuser
                    }
                    return render(request,'mass.html',contaxt)
                else:
                    if room.objects.filter(user=cuser).exists():
                        roy3 = room.objects.get(user=cuser)
                        roy3.croom = roy
                        roy3.save()
                    else:
                        roy4 = room(user=cuser,croom=roy)
                    
                        
                        roy4.save()
                    contaxt = {
                        'text':'you are no chat yet',
                        'paramiter':False
                    }
                    return render(request,'mass.html',contaxt)

            elif  mes.objects.filter(fuser=nroy).exists():
                if data.objects.filter(fuserr=nroy).exists():
                    if room.objects.filter(user=cuser).exists():
                        roy3 = room.objects.get(user=cuser)
                        roy3.croom = nroy
                        roy3.save()
                    else:
                        roy4 = room(user=cuser,croom=nroy)
                    
                        
                        roy4.save()
                    
                    messe = data.objects.filter(fuserr=nroy)
                    
                    contaxt = {
                        'messe':messe,
                        'paramiter':True
                    }
                    return render(request,'mass.html',contaxt)
                else:
                    if room.objects.filter(user=cuser).exists():
                        roy3 = room.objects.get(user=cuser)
                        roy3.croom = roy
                        roy3.save()
                    else:
                        roy4 = room(user=cuser,croom=roy)
                    
                        
                        roy4.save()
                    contaxt = {
                        'text':'you are no chat yet',
                        'paramiter':False
                    }
                    return render(request,'mass.html',contaxt)

            else:
                nmes = mes(user=cuser,fuser=roy)
                nmes.save()
                return render(request,'mass.html')
        else:
            return redirect('/')
    else:
        roomm =  room.objects.get(user=request.user)
        ttt = roomm.croom
        messe = data.objects.filter(fuserr=ttt)         
        contaxt = {
                    'messe':messe,
                    'paramiter':True
                    }
        return render(request,'mass.html',contaxt)

def newmass(request):
    roomm =  room.objects.get(user=request.user)
    ttt = roomm.croom
    owner = request.user
    messss = request.POST['newmass']
    nm = data(fuserr=ttt,owner=owner,masseage=messss)
    nm.save()
    return redirect('mass')   


    