from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name='index'),
path('login.html', views.login, name='login'),
path('logout.html', views.logout, name='logout'),
path('contacto.html', views.contacto, name='contacto'),
path('conocenos.html', views.conocenos, name='conocenos'),
path('servicios.html', views.servicios, name='servicios'),
path('compra.html', views.compra, name='compra'),
path('pago.html', views.pago, name='pago'),
path('comprador.html', views.comprador, name='comprador'),
path('vendedor.html',views.vendedor,name='vendedor'),
path('productos.html', views.productos, name='productos'),
]

