from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth

def index(request):
    return render(request,'eshop/index.html')

# def e404(request):
#     return render(request, 'eshop/404.html')

def SignUp(request):
    if request.method == "POST":
        form_register = SignUpForm(request.POST)
        if form_register.is_valid():
            
            # first_name = forms.cleaned_data
            # email = forms.cleaned_data.get('email')
            # raw_password = forms.cleaned_data.get('password')
            # user = authenticate(email=email, password=raw_password)
            messages.success(request, "Account created successfully!")
            form_register.save()
            return redirect('login')
        # return render(request, '/eshop/login.html', {'form':forms} )

    else:
        form_register = SignUpForm()
            
    return render(request, 'eshop/register.html', {'form_register':form_register} )


def user_login(request):

    if request.method == "POST":
        form_login = AuthenticationForm(data= request.POST)
        if form_login.is_valid():
                # uname = fm.cleaned_data['username']
            uemail = form_login.cleaned_data['username']
            upass = form_login.cleaned_data['password']
            user = authenticate(username=uemail, password=upass)
            user.set_password(upass)
            if user is not None:
                login(request,user)
                print("#3333333333333333",user)
                return redirect('index', { 'form_login':form_login})
    else:
        form_login  = AuthenticationForm()

    return render(request,"eshop/login.html",{'form_login':form_login })
    
# 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

# def RegisterLogin(request):
#     form = SignUpForm(request.POST)
#     if 'login' in request.POST:

        
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = auth.authenticate(request, email=email, password=password)
#         print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#         if user is not None:
#             auth.login(request, user)
#             print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#             messages.success(request, "You are logged in")
#             return redirect("index")
#         else:
#             messages.warning(
#                 request, "You are not authorised to access this page")

#     elif 'signup' in request.POST:
#         if form.is_valid():
#             form.save()
#             messages.success(request, "You are registered succesfully")
#         else:
#             print("invalid form details")
        
#     return render(request, 'eshop/login.html',{'form':form})
# def login(request):
#     form = SignUpForm(request.POST)
#     if request.method == "POST":
        
#         if request.POST.get('submit') == 'login':
#             # form = AuthenticationForm(request=request, data= request.POST)
#             if form.is_valid():
#                  email = request.POST.get('email')
#                  password = request.POST.get('password')
#                  user = authenticate(email=email, password=password)
#                  if user is not None:
#                      login(request,user)
#                      messages.success(request,'logged in successfully!!!')
#                      return redirect("index")
            

#         elif request.POST.get('submit') == 'signup':
            
#             if form.is_valid():
#                 messages.success(request, "Account created successfully!")
#                 form.save()
#                 return redirect('signup')
#             else:
#                 form = SignUpForm()

        
#     return render(request,'eshop/login.html',{'form':form})

