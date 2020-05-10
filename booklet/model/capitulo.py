# coding: utf-8

from google.appengine.ext import ndb
from libro import Libro

class Capitulo(ndb.Model):
    clave_libro = ndb.KeyProperty(kind=Libro)
    titulo = ndb.StringProperty(required=True)
    texto = ndb.StringProperty(required=True)
    fecha_creacion = ndb.DateProperty(auto_now_add=True)
    num_capitulo = ndb.IntegerProperty(required=True)

    @staticmethod
    def get_by_libro(clave):
        return Capitulo.query(Capitulo.clave_libro == ndb.Key(urlsafe=clave)).order(Capitulo.num_capitulo)

    @staticmethod
    def get(clave):
        return ndb.Key(urlsafe=clave).get()

