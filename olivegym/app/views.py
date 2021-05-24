from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from .models import Registration


# Create your views here.
def index(request):
    return render(request,'index.html')
    
def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def joining(request):
    return render(request,'join.html')

def joinsuccess(request):
    cn = request.POST.get('cname', 'default')
    cmobile = request.POST.get('mobile', 'default')
    cage = request.POST.get('age', 'default')
    ccity = request.POST.get('city', 'default')
    cstate = request.POST.get('state', 'default')
    ccountry = request.POST.get('country', 'default')
    caddress = request.POST.get('address', 'default')
    myregistration = Registration(name=cn, mobile=cmobile, age=cage, city=ccity, state=cstate, country=ccountry, address=caddress)
    myregistration.save()
    return HttpResponse('process done')
    
def calling(request):
    return render(request, 'call.html')

def messaging(request):
    return render(request, 'message.html')

def fees(request):
    return render(request, 'fees.html')


    
    
    
    
    # cn = request.POST.get('cname', 'default')
    # cmobile = request.POST.get('mobile', 'default')
    # cage = request.POST.get('age', 'default')
    # print(cn)
    # print(cmobile)
    # print(cage)
    # return HttpResponse("done")




    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('join') 
    # else:
    #     form = RegistrationForm()
    # context = {'c_form':form}
    # return render(request,'join.html',context)

