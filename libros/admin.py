from django.contrib import admin
from .models import Categoria, Imagen, Libro, Capitulo, Comentario, Opcion, Contenido

# , Autoevaluacion, Opcion


class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    list_filter = ('categoria','usuario')


class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'titulo', 'orden')


class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    list_filter = ('categoria', )


class OpcionAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'opcion', 'categoria')
    list_filter = ('categoria', )



# Register your models here.

admin.site.register(Categoria)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Comentario)
admin.site.register(Contenido)
admin.site.register(Opcion, OpcionAdmin)

