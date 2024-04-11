from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful sign-up
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html')

""" @login_required """
def homepage(request):
    return redirect(request, 'registration/home.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page
    return redirect('signup')