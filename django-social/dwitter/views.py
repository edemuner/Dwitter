from django.shortcuts import render
from .models import Profile

# Create your views here.


def dashboard(request):
    return render(request, "base.html")

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles":profiles})

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

def login(request):
    return render(request, "login.html")

# solução alternativa para obter os seguidores,
# utilizada antes de verificar a possibilidade de se usar o atributo related_name no model Profile
# def get_followers(pk):
#     return Profile.objects.filter(follows=pk)
