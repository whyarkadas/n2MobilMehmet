from django import forms  
from vehicles.models import Vehicle  
class VehicleForm(forms.ModelForm):  
    class Meta:  
        model = Vehicle  
        fields = ["plate_number", "register_date", "brand"]  
