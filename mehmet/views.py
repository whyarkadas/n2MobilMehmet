from django.shortcuts import render, redirect  
from mehmet.forms import VehicleForm  
from mehmet.models import Vehicle  
# Create your views here.  
def vehc(request):  
    if request.method == "POST":  
        form = VehicleForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/mehmet/show')  
            except:  
                pass  
    else:  
        form = VehicleForm()  
    return render(request,'new.html',{'form':form})  
def show(request):  
    vehicles = Vehicle.objects.all()  
    return render(request,"show.html",{'vehicles': vehicles})  
def edit(request, id):  
    vehicle = Vehicle.objects.get(id=id)  
    return render(request,'edit.html', {'vehicle': vehicle})  
def update(request, id):  
    vehicle = Vehicle.objects.get(id=id)  
    form = VehicleForm(request.POST, instance = vehicle)  
    if form.is_valid():  
       form.save()  
       return redirect("/mehmet/show")
    print (form.is_valid())
    print (form.errors)  
    return render(request, 'edit.html', {'vehicle': vehicle})  
def destroy(request, id):  
    vehicle = Vehicle.objects.get(id=id)  
    vehicle.delete()  
    return redirect("/mehmet/show")  
