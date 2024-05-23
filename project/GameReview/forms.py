from django import forms
from . import models

class AgregarReviewForm(forms.ModelForm):
    class Meta:
        model = models.GameReview
        fields = "__all__"


