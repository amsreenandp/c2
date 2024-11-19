from django.urls import path

from . import views

urlpatterns = [
    
   path('',views.Apiview, name='home'),
   path('create/',views.additems,name='add-item'),
   path('all/', views.viewitems, name='view_items'),
   path('update/<int:pk>/', views.updateitems, name='update-items'),
   path('item/<int:pk>/delete/', views.deleteitems, name='delete-items'),
]