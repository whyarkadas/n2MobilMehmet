from django import forms  
from mehmet.models import Vehicle  
class VehicleForm(forms.ModelForm):  
    class Meta:  
        model = Vehicle  
        fields = "__all__"  
