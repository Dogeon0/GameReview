
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
app_name = "Accounts"

urlpatterns = [
    path("login/",views.CustomLoginView.as_view(), name="Login"),
    path("logout/",LogoutView.as_view(template_name = "logout.html"),name="Logout"),
    path("register/",views.register,name="Register"),
    path('',views.accHome,name='Home'),
    path('profile/',views.profiles,name='Profile'),

    path('profile/edit',views.UserChange,name='EditProfile'),
    path('profile/password_change/',auth_views.PasswordChangeView.as_view(), name="PasswordChange"),
    path('profile/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="PasswordChangeDone"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)