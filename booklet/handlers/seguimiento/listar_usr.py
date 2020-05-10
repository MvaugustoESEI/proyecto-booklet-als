import webapp2
from model.libro import Libro
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.usuario_libro_seguido import UsuarioLibroSeguido


class ListaSeguimientoHandler(webapp2.RequestHandler):
    def get(self):
        lista_seguimiento = UsuarioLibroSeguido.get_by_user(users.get_current_user().email())
        libros = []

        for seguido in lista_seguimiento:
            libros.append(Libro.get(seguido.clave_libro.urlsafe()))

        valores_plantilla = {
            "libros": libros,
            "usr_logout": users.create_logout_url("/"),
            "usr_email": users.get_current_user().email()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/seguimiento/lista_mis_seguidos.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/seguimiento/listar_usr', ListaSeguimientoHandler)
], debug=True)
