from django.contrib import admin

# Register your models here.
from .models import Empleado, Secretaria,Empleado,Empleador, Vendedor,Comprador,Producto

admin.site.site_header = "PANEL  De la compañía"
admin.site.site_title  = "base-job ,entra y ponte al día"
admin.site.index_title  = 'oficina de gestión basejob'






admin.site.register(Producto)
class Productoadmin(admin.ModelAdmin):
    list_display = ('codigo','codigo_barra','image','categoria','nombre','referencia','descripcion','comprador','vendedor')

#



admin.site.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'dni', 'image','telefono','email','direccion' ,'sueldo','nºss')
#

admin.site.register(Empleador)
class EmpleadorAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Apellido', 'dni', 'image','telefono','email','direccion','nºss')
#

#

admin.site.register(Secretaria)
#
admin.site.register(Comprador)
class CompradorAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'id', 'email','direccion' , 'telefono','targeta_de_credito','NIF')
#
admin.site.register(Vendedor)
class vendedorAdmin(admin.ModelAdmin):
    list_display = ('name','image', 'dniz', 'email','direccion' , 'telefono','targeta_de_credito','NIF')
#


