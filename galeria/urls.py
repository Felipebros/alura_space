from django.urls import path
from galeria.views import index, index_outra_maneira, imagem

urlpatterns = [
    path("", index, name='index'),
    path("index2", index_outra_maneira),
    path("imagem/", imagem, name='imagem'),
]
