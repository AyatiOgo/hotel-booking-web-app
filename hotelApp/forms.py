from django import forms

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
