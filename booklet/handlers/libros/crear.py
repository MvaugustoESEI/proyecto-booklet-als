import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.libro import Libro
import time


class CrearLibroHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
            "usr_logout": users.create_logout_url("/"),
            "usr_email": users.get_current_user().email()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/libros/crear_libro.html", **valores_plantilla))

    def post(self):
        usr = users.get_current_user()

        if usr:
            usr_email = usr.email()

            titulo = self.request.get("edTituloLibro", "")
            generos = self.request.get_all("edGeneros")
            sinopsis = self.request.get("edSinopsis", "")

            if len(titulo.strip()) > 0 and len(generos) > 0 and len(sinopsis.strip()) > 0:
                libro = Libro(titulo=titulo, generos=", ".join(generos), sinopsis=sinopsis, autor=usr_email, num_capitulos=0)
                libro.put()

            time.sleep(1)

            return self.redirect("/libros/listar_usr")


app = webapp2.WSGIApplication([
    ('/libros/crear', CrearLibroHandler)
], debug=True)