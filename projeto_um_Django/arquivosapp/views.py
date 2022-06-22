from django.shortcuts import render, HttpResponse #-> Interpreta o parametro e retorna como HTTP

# Create your views here.
def helloworld(request, nome):
    return HttpResponse(f'<h1>Hello, World! Its me again :) \nNice to see you here {nome}</h1>')