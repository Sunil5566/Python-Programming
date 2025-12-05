from django import forms

from .models import Reservation

class Reservation(forms.modelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        