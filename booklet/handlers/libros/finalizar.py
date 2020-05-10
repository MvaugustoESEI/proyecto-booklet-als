import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.libro import Libro
from model.capitulo import Capitulo
import time
from datetime import date


class TerminarLibroHandler(webapp2.RequestHandler):
    def get(self):
        libro = Libro.get(self.request.GET["id"])

        if libro.autor != users.get_current_user().email() or libro.fecha_finalizacion:
            return self.redirect("/")

        libro.fecha_finalizacion = date.today()
        libro.put()

        time.sleep(1)

        return self.redirect("/libros/listar_usr")


app = webapp2.WSGIApplication([
    ('/libros/finalizar', TerminarLibroHandler)
], debug=True)