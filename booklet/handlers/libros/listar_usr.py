# coding: utf-8

import webapp2
from model.libro import Libro
from webapp2_extras import jinja2
from webapp2_extras.users import users


class ListaLibrosHandler(webapp2.RequestHandler):
    def get(self):
        libros = Libro.query(Libro.autor == users.get_current_user().email())

        valores_plantilla = {
            "libros": libros,
            "usr_logout": users.create_logout_url("/"),
            "usr_email": users.get_current_user().email()
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("/libros/lista_mis_libros.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/libros/listar_usr', ListaLibrosHandler)
], debug=True)
