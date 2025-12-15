from django import forms

class BookingForm(forms.Form):
    guest_name = forms.CharField(max_length=100)
    guest_email = forms.EmailField()
    guest_phone = forms.CharField(max_length=20)
    