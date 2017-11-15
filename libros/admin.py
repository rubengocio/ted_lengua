from django.contrib import admin
from .models import Categoria, Imagen, Libro, Capitulo, Comentario, Opcion, Contenido, Pregunta, TipoPregunta, \
    Autoevaluacion


# , Autoevaluacion, Opcion


class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    list_filter = ('categoria','usuario')


class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'libro', 'titulo', 'orden')


class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria')
    list_filter = ('categoria', )


class OpcionHeadInLine(admin.TabularInline):
    model = Opcion
    extra = 1


class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'texto', 'tipo_pregunta', )
    list_filter = ('tipo_pregunta', )
    inlines = [OpcionHeadInLine]


class TipoPreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto', 'categoria', 'orden',)


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Imagen, ImagenAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Comentario)
admin.site.register(Contenido)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(TipoPregunta, TipoPreguntaAdmin)
admin.site.register(Autoevaluacion)
