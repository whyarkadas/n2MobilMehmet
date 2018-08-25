from django.contrib import admin  
from django.urls import path  
from mehmet import views  
urlpatterns = [  
#    path('admin/', admin.site.urls),  
    path('', views.show),
    path('vehc', views.vehc),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  
