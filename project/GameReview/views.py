from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from GameReview import forms,models
from GameReview.models import *
from GameReview.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def pageIndex(request):
    return render(request,"pages.html")

def home(request):
    return render(request,"index.html")

@login_required
def about(request):
    return render(request,"about.html")

class ReviewList(LoginRequiredMixin,ListView):
    model = models.GameReview
    context_object_name = "reviews"
    template_name = "reviewList.html"

class ReviewAdd(LoginRequiredMixin,CreateView):
    model = models.GameReview
    template_name = "reviewAdd.html"
    success_url = reverse_lazy('GameReview:ReviewListar')
    fields = "__all__"

class ReviewDetail(LoginRequiredMixin,DetailView):
    model = models.GameReview
    template_name = "reviewDetail.html"

class ReviewEdit(LoginRequiredMixin,UpdateView):
    model = models.GameReview
    template_name = "reviewUpdate.html"
    success_url = reverse_lazy('GameReview:ReviewListar')
    fields = "__all__"

class ReviewDelete(LoginRequiredMixin,DeleteView):
    model = models.GameReview
    template_name = "reviewDelete.html"
    success_url = reverse_lazy('GameReview:ReviewListar')