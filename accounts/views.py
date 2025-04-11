from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

#المستخدم وصل بطريقة post
def login_view(request):
    if request.method=='POST':    #يتحقق اذا المستخدم ادخل بطريقة البوست
       form=AuthenticationForm(request,data=request.POST)
       if form.is_valid():
           user=form.get_user()
           login(request,user) 
           return redirect('checkout')
    else:                     #المستخدم وصل بطريقة GET
        form=AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def register(request):
    if request.method=='POST':  
        form=RegisterForm(request.POST)
        if form.is_valid():
           user=form.save()
           login(request,user) #بعد ما سجل يرجع يسجل دخول
           return redirect('index')#ثم يرجع للصفحة الرئيسية لمواصلة التسوق
    else:
        form=RegisterForm()
    return render(request,'account/register.html',{'form':form})


#logoutدالة
def logout_view(request):
    logout(request)
    return redirect('index')
    
       



