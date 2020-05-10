import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.capitulo import Capitulo
from model.libro import Libro
import time


class EliminarCapituloHandler(webapp2.RequestHandler):
    def get(self):
        capitulo = Capitulo.get(self.request.GET["id"])
        libro = Libro.get(capitulo.clave_libro.urlsafe())

        if libro.autor != users.get_current_user().email():
            return self.redirect("/")

        num_capitulo = capitulo.num_capitulo

        capitulo.key.delete()

        capitulos = Capitulo.get_by_libro(libro.key.urlsafe())
        libro.num_capitulos = libro.num_capitulos - 1
        libro.put()

        i = 1
        for cap in capitulos:
            cap.num_capitulo = i
            cap.put()
            i += 1

        time.sleep(1)

        return self.redirect("/libros/ver?id=" + libro.key.urlsafe() + "&volver=" + self.request.GET["volver"])


app = webapp2.WSGIApplication([
    ('/capitulos/eliminar', EliminarCapituloHandler)
], debug=True)