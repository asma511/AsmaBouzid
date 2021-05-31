from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('visage/', views.visag, name="visage"),
	path('sante/', views.sant, name="sante"),
	path('cheveux/', views.cheveu, name="cheveux"),
	path('corps/', views.corp, name="corps"),
]