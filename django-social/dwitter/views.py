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
    return render(request, "dwitter/profile.html", {"profile": profile})
    # return render(request, "dwitter/profile.html", {"profile": profile, "followers":get_followers(pk)})

# solução alternativa para obter os seguidores,
# utilizada antes de verificar a possibilidade de se usar o atributo related_name no model Profile
# def get_followers(pk):
#     return Profile.objects.filter(follows=pk)
