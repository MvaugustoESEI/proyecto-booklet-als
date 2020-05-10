import webapp2
from model.libro import Libro
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.capitulo import Capitulo


class DetallesCapituloHandler(webapp2.RequestHandler):
    def get(self):

        capitulo = Capitulo.get(self.request.GET["id"])
        libro = Libro.get(capitulo.clave_libro.urlsafe())
        parrafos = capitulo.texto.split('\n')

        siguiente_capitulo = Capitulo.query(Capitulo.clave_libro == libro.key, Capitulo.num_capitulo == capitulo.num_capitulo + 1)
        siguiente_capitulo_key = siguiente_capitulo.fetch(1)[0].key.urlsafe() if len(siguiente_capitulo.fetch(1)) > 0 else None

        anterior_capitulo = Capitulo.query(Capitulo.clave_libro == libro.key, Capitulo.num_capitulo == capitulo.num_capitulo - 1)
        anterior_capitulo_key = anterior_capitulo.fetch(1)[0].key.urlsafe() if len(anterior_capitulo.fetch(1)) > 0 else None

        valores_plantilla = {
            "libro": libro,
            "usr_email": users.get_current_user().email(),
            "usr_logout": users.create_logout_url("/"),
            "capitulo": capitulo,
            "parrafos": parrafos,
            "volver": self.request.GET["volver"],
            "siguiente_capitulo_key": siguiente_capitulo_key,
            "anterior_capitulo_key": anterior_capitulo_key
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/capitulos/ver_capitulo.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/capitulos/ver', DetallesCapituloHandler)
], debug=True)