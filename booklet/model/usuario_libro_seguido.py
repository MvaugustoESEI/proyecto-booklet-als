# coding: utf-8

from google.appengine.ext import ndb
from libro import Libro

class UsuarioLibroSeguido(ndb.Model):
    clave_libro = ndb.KeyProperty(kind=Libro)
    seguidor = ndb.StringProperty(required=True)

    @staticmethod
    def get_by_libro(clave):
        return UsuarioLibroSeguido.query(UsuarioLibroSeguido.clave_libro == ndb.Key(urlsafe=clave))

    @staticmethod
    def get_by_user(email):
        return UsuarioLibroSeguido.query(UsuarioLibroSeguido.seguidor == email)

    @staticmethod
    def get_by_libro(clave):
        return UsuarioLibroSeguido.query(UsuarioLibroSeguido.clave_libro == clave)

    @staticmethod
    def get(clave):
        return ndb.Key(urlsafe=clave).get()
