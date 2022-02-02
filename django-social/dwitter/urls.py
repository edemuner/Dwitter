from django.urls import path
from .views import dashboard, profile_list, profile, login_page, submit_login, view_logout

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("login/", login_page, name="login_page"),
    path("login/submit", submit_login, name="submit_login"),
    path("logout/", view_logout, name="view_logout"),
]