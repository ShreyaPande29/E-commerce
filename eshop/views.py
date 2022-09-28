from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def index(request):
    return render(request,'eshop/index.html')

# def e404(request):
#     return render(request, 'eshop/404.html')

def SignUp(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            
            # first_name = forms.cleaned_data
            # email = forms.cleaned_data.get('email')
            # raw_password = forms.cleaned_data.get('password')
            # user = authenticate(email=email, password=raw_password)
            messages.success(request, "Account created successfully!")
            forms.save()
            return redirect('/')
        # return render(request, '/eshop/login.html', {'form':forms} )

    else:
        forms = SignUpForm()
            
    return render(request, 'eshop/login.html', {'form':forms} )


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data= request.POST)
            if fm.is_valid():
                # uname = fm.cleaned_data['username']
                uemail = fm.cleaned_data['email']
                upass = fm.cleaned_data['password']
                user = authenticate(email=uemail, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully!!!')
                    return redirect("index")
        else:
            fm = AuthenticationForm()
        return render(request,"eshop/login.html",{'form':fm})
    else:
        return redirect('index')
