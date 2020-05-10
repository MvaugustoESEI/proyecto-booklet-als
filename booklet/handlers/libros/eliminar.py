import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.libro import Libro
from model.capitulo import Capitulo
from model.usuario_libro_seguido import UsuarioLibroSeguido
import time


class EliminarLibroHandler(webapp2.RequestHandler):
    def get(self):
        libro = Libro.get(self.request.GET["id"])
        capitulos = Capitulo.get_by_libro(self.request.GET["id"])
        seguimiento = UsuarioLibroSeguido.get_by_libro(libro.key)

        if libro.autor != users.get_current_user().email():
            return self.redirect("/")

        libro.key.delete()
        for capitulo in capitulos:
            capitulo.key.delete()

        for seguidor in seguimiento:
            seguidor.key.delete()

        time.sleep(1)

        return self.redirect("/libros/listar_usr")


app = webapp2.WSGIApplication([
    ('/libros/eliminar', EliminarLibroHandler)
], debug=True)