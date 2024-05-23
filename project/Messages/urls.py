from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = "Messages"

urlpatterns = [
    path('', views.inbox, name='Inbox'),
    path('sent/', views.enviadosMensaje, name='MsjEnviados'),
    path('send/', views.enviarMensaje, name='MsjEnviar'),
    path('<int:pk>/', views.leerMensaje, name='MsjLeer'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
