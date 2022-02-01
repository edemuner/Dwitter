from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import DweetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.

@login_required(login_url='/login/')
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(request, "dwitter/dashboard.html", {"form": form, "dweets":followed_dweets})

@login_required(login_url='/login/')
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles":profiles})

@login_required(login_url='/login/')
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
    # return render(request, "dwitter/profile.html", {"profile": profile, "followers":get_followers(pk)})

def login_page(request):
    return render(request, "dwitter/login.html")

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return redirect('/')

# solução alternativa para obter os seguidores,
# utilizada antes de verificar a possibilidade de se usar o atributo related_name no model Profile
# def get_followers(pk):
#     return Profile.objects.filter(follows=pk)
