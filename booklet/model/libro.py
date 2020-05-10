# coding: utf-8

from google.appengine.ext import ndb


class Libro(ndb.Model):
    autor = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)
    generos = ndb.StringProperty(required=True)
    sinopsis = ndb.StringProperty(required=True)
    fecha_creacion = ndb.DateProperty(auto_now_add=True)
    num_capitulos = ndb.IntegerProperty(required=True)
    fecha_finalizacion = ndb.DateProperty()

    @staticmethod
    def get(clave):
        return ndb.Key(urlsafe=clave).get()
