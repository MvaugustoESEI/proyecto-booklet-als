import webapp2
from model.libro import Libro
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.capitulo import Capitulo
from model.usuario_libro_seguido import UsuarioLibroSeguido


class DetallesLibroHandler(webapp2.RequestHandler):
    def get(self):

        clave = self.request.GET["id"]

        libro = Libro.get(self.request.GET["id"])

        valores_plantilla = {
            "seguido": UsuarioLibroSeguido.get_by_user(users.get_current_user().email()).count() > 0,
            "libro": libro,
            "usr_email": users.get_current_user().email(),
            "usr_logout": users.create_logout_url("/"),
            "generos": ["FANTASIA", "SCIFI", "MISTERIO", "ROMANCE", "AMOR", "HISTORIA"],
            "capitulos": Capitulo.get_by_libro(libro.key.urlsafe()),
            "url_volver": "/libros/listar_usr" if self.request.GET["volver"] == "user" else "/seguimiento/listar_usr" if self.request.GET["volver"] == "seguimiento" else "/",
            "volver": self.request.GET["volver"]
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/libros/ver_libro.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/libros/ver', DetallesLibroHandler)
], debug=True)
