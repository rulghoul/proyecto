from django.contrib import admin


from .models import TipoSalon, Direccion, Servicio, Imagen, Salon

admin.site.register(TipoSalon)
admin.site.register(Direccion)
admin.site.register(Servicio)
admin.site.register(Imagen)
admin.site.register(Salon)