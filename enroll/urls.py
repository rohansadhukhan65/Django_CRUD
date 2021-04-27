from django.urls import path
from django.contrib import admin
from enroll import views

urlpatterns = [
    path('', views.UserAddShow.as_view(), name='addandshow'),
    path('delete/<str:id>/', views.UserDel.as_view(), name='delete_Data'),
    path('<str:id>/', views.editDAt.as_view(), name='update_data'),

 

   

]
