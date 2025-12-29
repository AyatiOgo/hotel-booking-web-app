from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import HotelUsers




class BookingForm(forms.Form):
    guest_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md " ,
        "placeholder":"Input Full Name",
    }) )
    guest_email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md " ,
        "placeholder":"Input Email",
    }))
    guest_phone = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md " ,
        "placeholder":"Input Phone Number",
    }))

class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Username"
    }))
    full_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Full Name"
    }))
    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Username"
    }))
    email = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Email"
    }))
    phone_no = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Phone Number"
    }))
    phone_no = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Phone Number"
    }))
    password1 = forms.CharField(max_length=100, label="Password", widget= forms.PasswordInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Password"
    }))
    password2 = forms.CharField(max_length=100, label="Confirm Password", widget= forms.PasswordInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Confirm Password",
    }))


    class Meta:
        model = HotelUsers
        fields = ["username", "full_name", "email", "phone_no", "password1", "password2"]

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(max_length=100, widget= forms.TextInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input username"
    }))

    password = forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={
        "class":"w-full border border-[#F0F0F0] bg-[#F5F5F5] py-2 px-4 rounded-md ",
        "placeholder" : "Input Password"
    }))

    class Meta:
        Model = HotelUsers
        fields = ["username", "password"]

