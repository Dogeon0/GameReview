from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from Accounts.forms import CustomAuthenticationForm, CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from Accounts.models import *
from Accounts.forms import *

# Create your views here.
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "login.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # The profile will be created by the signal
            profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('GameReview:Index')
    else:
        form = CustomUserCreationForm()
        profile_form = ProfileForm()

    return render(request, "register.html", {
        "form": form,
        "profile_form": profile_form
    })

@login_required
def accHome(request):
    return render(request,"accHome.html")

@login_required
def profiles(request):
    profile = request.user.profile
    return render(request, "profile.html", {"profile": profile})


@login_required
def UserChange(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('Accounts:Profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, "userchange.html", {
        "form": form,
        "profile_form": profile_form
    })

@login_required
def password_change(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update session with new password hash
            return redirect("Accounts:PasswordChangeDone")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "passwordChange.html", {"form": form})

@login_required
def password_change_done(request):
    return render(request, "passwordChangeDone.html")
