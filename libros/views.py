import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Categoria, Imagen, Libro, Capitulo, Comentario, Contenido
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def category_list(request):
    template_name = 'libros/category_list.html'
    category_list = Categoria.objects.all()
    context = {
        'category_list': category_list,
        'menu': 'eje'
    }

    return render(request,template_name,context)

@login_required
def new_book(request, slug, id_book=None, id_chapter=None):
    template_name = 'libros/book_form.html'
    category = Categoria.objects.get(slug=slug)
    images_list = []
    image = Imagen()
    images_list = image.get_images_by_paginate(category)
    anterior = None
    actual = 0
    siguiente = None

    if images_list:
        first = images_list[0][0].id

    capitulo = ''
    if id_chapter:
        capitulo = id_chapter
        anterior = int(capitulo) - 1
        actual = int(capitulo)
        siguiente = int(capitulo) + 1

    book = Libro()
    capitulo_actual = Capitulo()

    if id_book and id_book != '':
        book = Libro.objects.get(id=id_book)

    if id_chapter and id_chapter != '' and Capitulo.objects.filter(libro=book,orden=id_chapter).exists():
        capitulo_actual = Capitulo.objects.get(libro = book, orden=id_chapter)

    if request.method == 'POST':
        id_book = request.POST.get('id_book')
        id_chapter = request.POST.get('id_chapter')
        capitulo = request.POST.get('capitulo')
        titulo = request.POST.get('txtTitulo')
        texto = request.POST.get('txtTexto')
        id_imagen = request.POST.get('id_imagen')
        chkPublico = request.POST.get('chkPublico')

        es_publico = False
        if chkPublico:
            es_publico = True

        user = request.user
        imagen = Imagen.objects.get(id=id_imagen)

        if id_book and id_book != '' and id_book != 'None' and Libro.objects.filter(id=id_book).exists():
            book = Libro.objects.get(id=id_book)

        if id_chapter and id_chapter != '' and id_chapter != 'None' and Capitulo.objects.filter(libro=book,orden=id_chapter).exists():
            capitulo_actual = Capitulo.objects.get(libro=book,orden=id_chapter)

        if id_chapter is None or id_chapter == '' or id_chapter == 'None':
            book.titulo = titulo
            book.introduccion = texto
            book.usuario = user
            book.categoria = category
            book.imagen = imagen
            book.es_publico = es_publico
            book.save()
            anterior = None
            actual = 0
            siguiente = 1
        else:
            book = Libro.objects.get(id=id_book)
            capitulo_actual.titulo = titulo
            capitulo_actual.texto = texto
            capitulo_actual.libro = book
            capitulo_actual.imagen = imagen
            capitulo_actual.orden = id_chapter
            capitulo_actual.save()
            capitulo = id_chapter
            anterior = int(capitulo) - 1
            actual = int(capitulo)
            siguiente = int(capitulo) + 1


    context = {
        'images_list': images_list,
        'capitulo': capitulo,
        'category': category,
        'book': book,
        'capitulo_actual': capitulo_actual,
        'id_chapter': id_chapter,
        'first': first,
        'menu': 'eje',
        'anterior': anterior,
        'actual': actual,
        'siguiente': siguiente
    }

    return render(request, template_name, context)


def home(request):
    template_name = 'libros/index.html'

    libros_destacados = Libro.get_destacados()

    context = {
        'libros_destacados': libros_destacados,
        'menu': 'ind'
    }

    return render(request, template_name, context)


def list_book(request, slug):
    template_name = 'libros/book_list.html'
    category = Categoria.objects.get(slug=slug)
    books = Libro.objects.filter(categoria=category)

    user = request.user
    if not user.is_anonymous():
        if request.user.is_staff is False:
            books = books.filter(Q(usuario=user) | Q(es_publico=True))
    else:
        books = books.filter(es_publico=True)

    context = {
        'category': category,
        'books': books,
        'menu': 'eje'
    }
    return render(request, template_name, context)


def read_book(request, slug, id_book=None, id_chapter=None):
    template_name = 'libros/read_book.html'
    category = Categoria.objects.get(slug=slug)
    book = Libro.objects.get(id=id_book)
    chapter = Capitulo.objects.filter(libro=book, orden=id_chapter).first()
    chapters = Capitulo.objects.filter(libro=book).order_by('orden')
    comments = Comentario.objects.filter(libro=book).order_by('-date_created')

    siguiente = None
    anterior = None
    if chapter:
        siguiente = chapter.orden + 1
        anterior  = chapter.orden - 1
        actual = chapter.orden
        if not Capitulo.objects.filter(libro=book, orden=siguiente).exists():
            siguiente = None
        if not Capitulo.objects.filter(libro=book, orden=anterior).exists():
            anterior = None

    context = {
        'category': category,
        'book': book,
        'chapter': chapter,
        'siguiente': siguiente,
        'anterior': anterior,
        'chapters': chapters,
        'comments': comments,
        'actual': actual,
        'menu': 'eje'
    }
    return render(request, template_name, context)


def register(request):
    template_name = 'libros/register.html'

    if request.method == 'POST':
        user = User()

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = username
        password = request.POST.get('password')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.set_password(password)

        if not (User.objects.filter(username=username).exists()):
            grupo = Group.objects.get(name='Alumno')
            user.save()
            user.groups.add(grupo)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = 'libros/index.html'

    return render(request, template_name)


def student_list(request):
    template_name = 'libros/student_list.html'

    group = Group.objects.get(name='Alumno')
    students = User.objects.filter(groups=group)

    context = {
        'students': students,
        'menu': 'alu'
    }
    return render(request, template_name, context)

def editor(request):
    template_name = 'libros/wysiwyg.html'
    return render(request, template_name)


def student_books(request, student_id):
    student = User.objects.get(pk=student_id)
    books = Libro.objects.filter(usuario=student)
    books_json = []

    for book in books:
        row = {
            'titulo': book.titulo,
            'categoria': book.categoria.nombre,
            'fecha': book.date_created.strftime('%m/%d/%Y'),
            'link': book.categoria.slug + '/leer-libro/' + str(book.id) + '/1',
            'calificacion': book.calificacion
        }
        books_json.append(row)

    return JsonResponse({'books': books_json})


@csrf_exempt
def calificar(request):
    if request.method == 'POST':
        calificacion = request.POST.get('calificacion')
        id_book = request.POST.get('id_book')
        libro = Libro.objects.get(pk=id_book)

        if calificacion == '':
            calificacion = None
        libro.calificacion = calificacion
        libro.save()

    return JsonResponse({'status': 'ok'})

@csrf_exempt
def comentar(request):

    if request.method == 'POST':
        texto = request.POST.get('comentario')
        id_book = request.POST.get('id_book')
        libro = Libro.objects.get(pk=id_book)
        usuario = request.user
        comentario = Comentario()
        comentario.libro = libro
        comentario.comentario = texto
        comentario.usuario = usuario
        comentario.save()

    return JsonResponse({'status': 'ok'})


def content(request):

    contenido = None
    if request.method == 'GET':
        contenido = Contenido.objects.filter(numero=1).first()

    if request.method == 'POST':
        if Contenido.objects.filter(numero=1).exists():
            contenido = Contenido.objects.get(numero=1)
        else:
            contenido = Contenido()
            contenido.numero = 1
            contenido.usuario = request.user

        texto = request.POST.get('txtArea')
        contenido.texto = texto
        contenido.save()

    context = {
        'content': contenido,
        'menu': 'con'
    }

    return render(request, 'libros/content.html', context)


def autoevaluate(request):
    context = {
        'menu': 'eva'
    }

    return render(request, 'libros/autoevaluate.html', context)


def help(request):
    context = {
        'menu': 'ayu'
    }

    return render(request, 'libros/help.html', context)
