import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.libro import Libro
from model.capitulo import Capitulo
import time


class CrearCapituloHandler(webapp2.RequestHandler):
    def get(self):

        libro = Libro.get(self.request.GET["libro"])

        valores_plantilla = {
            "usr_email": users.get_current_user().email(),
            "usr_logout": users.create_logout_url("/"),
            "libro": libro,
            "volver": self.request.GET["volver"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/capitulos/crear_capitulo.html", **valores_plantilla))

    def post(self):
        libro = Libro.get(self.request.GET["libro"])
        titulo = self.request.get("edTituloCapitulo", "")
        texto = self.request.get("edTexto", "")
        num_capitulo = Capitulo.get_by_libro(libro.key.urlsafe()).count() + 1

        if libro.autor != users.get_current_user().email():
            return self.redirect("/")

        if len(titulo.strip()) > 0 and len(texto.strip()) > 0 and num_capitulo > 0:
            capitulo = Capitulo(titulo=titulo, texto=texto, clave_libro=libro.key, num_capitulo=num_capitulo)
            libro.num_capitulos += 1
            if capitulo.put():
                libro.put()

        time.sleep(1)

        return self.redirect("/libros/ver?id=" + self.request.GET["libro"] + "&volver=" + self.request.GET["volver"])


app = webapp2.WSGIApplication([
    ('/capitulos/crear', CrearCapituloHandler)
], debug=True)