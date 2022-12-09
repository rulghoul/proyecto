from django.contrib import admin


from .models import TipoActividad, TipoEvento, TipoServicio, Foto

admin.site.register(TipoActividad)
admin.site.register(TipoEvento)
admin.site.register(TipoServicio)
admin.site.register(Foto)