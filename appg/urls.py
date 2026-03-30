from django.urls import path
from appg import views

urlpatterns={
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('shop/',views.shop,name='shop'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='news'),
    path('single-news/',views.news,name='single-news'),
    path('checkout/',views.shop,name='checkout'),
    path('single-product/',views.shop,name='single-product'),
    path('cart/',views.shop,name='cart'),
    path('404/',views.shop,name='404'),
    path('index2/',views.home,name='index2'),
    path('index3/',views.home,name='index3'),



}