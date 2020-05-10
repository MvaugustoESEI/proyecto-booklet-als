import webapp2
from model.libro import Libro
from model.usuario_libro_seguido import UsuarioLibroSeguido
from webapp2_extras import jinja2
from webapp2_extras.users import users
import time
from datetime import date


class SeguirHandler(webapp2.RequestHandler):
    def get(self):

        libro = Libro.get(self.request.GET["libro"])

        if libro.autor == users.get_current_user().email() or UsuarioLibroSeguido.query(UsuarioLibroSeguido.clave_libro == libro.key, UsuarioLibroSeguido.seguidor == users.get_current_user().email()).count() > 0:
            return self.redirect("/")

        seguimiento = UsuarioLibroSeguido(clave_libro=libro.key, seguidor=users.get_current_user().email())
        seguimiento.put()

        time.sleep(1)

        return self.redirect("/libros/ver?id=" + libro.key.urlsafe() + "&volver=" + self.request.GET["volver"])


app = webapp2.WSGIApplication([
    ('/seguimiento/seguir', SeguirHandler)
], debug=True)
