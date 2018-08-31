from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from brands.forms import BrandForm  
from brands.models import Brand 
# Create your views here.  
def new(request):  
    if request.method == "POST":  
        form = BrandForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/brands/show')  
                 
            except:  
                pass  
    else:  
        form = BrandForm()  
    return render(request,'brands_new.html',{'form':form})  
def show(request):  
    brands = Brand.objects.all()  
    return render(request,"brands_show.html",{'brands': brands})  
def edit(request, id):  
    brands = Brand.objects.get(id=id)  
    return render(request,'brands_edit.html', {'brands': brands})  
def update(request, id):  
    brands = Brand.objects.get(id=id)  
    form = BrandForm(request.POST, instance = brands)  
    if form.is_valid():  
       form.save()  
       return redirect("/brands/show")
    print (form.is_valid())
    print (form.errors)  
    return render(request, 'brands_edit.html', {'brands': brands})  
def destroy(request, id):  
    brand = Brand.objects.get(id=id)  
    brand.delete()  
    return redirect("/brands/show")  
