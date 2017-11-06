from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^categorias/$', category_list, name='categories'),
    #url(r'^categorias/(?P<slug>[\w_-]+)/$', new_book, name='new_book'),
    url(r'^categorias/(?P<slug>[\w_-]+)/$', list_book, name='list_book'),
    url(r'^categorias/(?P<slug>[\w_-]+)/libro/$', new_book ),
    url(r'^categorias/(?P<slug>[\w_-]+)/libro/(?P<id_book>[0-9]+)/$', new_book ),
    url(r'^categorias/(?P<slug>[\w_-]+)/libro/(?P<id_book>[0-9]+)/(?P<id_chapter>[0-9]+)/$', new_book ),
    url(r'^categorias/(?P<slug>[\w_-]+)/leer-libro/(?P<id_book>[0-9]+)/(?P<id_chapter>[0-9]+)/$', read_book ),
    url(r'^alumnos/$', student_list, name='students'),
    url(r'^alumno/(?P<student_id>\d+)/$', student_books),
    url(r'^calificar/$', calificar),
    url(r'^comentar/$', comentar),
    url(r'^editor/$', editor),
    url(r'^contenido/$', content, name='content'),
    url(r'^autoevaluacion/$', autoevaluate, name='autoevaluacion'),
    url(r'^ayuda/$', help, name='ayuda'),
    url(r'^$', home, name='home'),


]
