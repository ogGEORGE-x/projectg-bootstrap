from django.urls import path
from appg import views

urlpatterns={
    path('',views.home,name='home'),

}