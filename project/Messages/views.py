# messages/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import User

@login_required
def inbox(request):
    messages = Message.objects.filter(receptor=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def enviadosMensaje(request):
    messages = Message.objects.filter(emisor=request.user).order_by('-timestamp')
    return render(request, 'enviadosMensaje.html', {'messages': messages})

@login_required
def enviarMensaje(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.emisor = request.user
            message.save()
            return redirect('Messages:Inbox')
    else:
        form = MessageForm()
    return render(request, 'enviarMensaje.html', {'form': form})

@login_required
def leerMensaje(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.receptor != request.user and message.emisor != request.user:
        return redirect('Messages:Inbox')
    if message.receptor == request.user:
        message.leido = True
        message.save()
    return render(request, 'leerMensaje.html', {'message': message})
