# messages/models.py

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    emisor = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    tema = models.CharField(max_length=255)
    cuerpo = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensaje de {self.emisor} a {self.receptor} - {self.tema}"
