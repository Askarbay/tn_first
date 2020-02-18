from django.urls import path, include
from zakaz import views

urlpatterns = [
    path('basket_adding/', views.basket_adding, name="basket_adding"),
    path('basket_adding_doc/', views.basket_adding_doc, name="basket_adding_doc"),

]