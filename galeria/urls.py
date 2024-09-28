from django.urls import path
from galeria.views import index, index_outra_maneira

urlpatterns = [
    path("", index),
    path("index2", index_outra_maneira),
]
