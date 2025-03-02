from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    UF = UserForm()
    d = {'UF': UF}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            email = UFDO.cleaned_data.get('email')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save() 
            send_mail(
                'Hello,',
                'Hello Miss Soumyashree Jena🥰',
                'deepankarmali2001@gmail.com',
                [email],
                fail_silently=False
            ) 
            return HttpResponse('Done............')
        return HttpResponse('invalid data')
    return render(request,'register.html', d)