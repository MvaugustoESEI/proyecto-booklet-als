import webapp2
from model.libro import Libro
from model.capitulo import Capitulo
from webapp2_extras import jinja2
from webapp2_extras.users import users
import time
from datetime import date


class EditarCapituloHandler(webapp2.RequestHandler):
    def get(self):
        capitulo = Capitulo.get(self.request.GET["id"])
        libro = Libro.get(capitulo.clave_libro.urlsafe())

        valores_plantilla = {
            "capitulo": capitulo,
            "libro": libro,
            "volver": self.request.GET["volver"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/capitulos/editar_capitulo.html", **valores_plantilla))

    def post(self):
        capitulo = Capitulo.get(self.request.GET["id"])
        libro = Libro.get(capitulo.clave_libro.urlsafe())

        titulo = self.request.get("edTituloCapitulo", "")
        texto = self.request.get("edTexto", "")
        num_capitulo = Capitulo.get_by_libro(libro.key.urlsafe()).count() + 1

        if libro.autor != users.get_current_user().email():
            return self.redirect("/")

        if len(titulo.strip()) > 0 and len(texto.strip()) > 0 and num_capitulo > 0:

            capitulo.texto = texto;
            capitulo.titulo = titulo;

            capitulo.put()

        time.sleep(1)

        return self.redirect("/capitulos/editar?id=" + self.request.GET["id"] + "&volver=" + self.request.GET["volver"])


app = webapp2.WSGIApplication([
    ('/capitulos/editar', EditarCapituloHandler)
], debug=True)
