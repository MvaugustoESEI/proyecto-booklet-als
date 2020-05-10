import webapp2
from model.libro import Libro
from webapp2_extras import jinja2
from webapp2_extras.users import users
import time
from datetime import date


class DetallesLibroHandler(webapp2.RequestHandler):
    def post(self):

        clave = self.request.GET["id"]

        libro = Libro.get(self.request.GET["id"])

        if libro.autor != users.get_current_user().email():
            return self.redirect("/")

        libro.titulo = self.request.get("edTituloLibro", "")
        libro.generos = ', '.join(self.request.get_all("edGeneros"))
        libro.sinopsis = self.request.get("edSinopsis", "")

        libro.put()

        time.sleep(1)

        return self.redirect("/libros/ver?id=" + libro.key.urlsafe() + "&volver=" + self.request.GET["volver"])


app = webapp2.WSGIApplication([
    ('/libros/editar', DetallesLibroHandler)
], debug=True)
