import pathlib
import unittest

RAIZ = pathlib.Path(__file__).resolve().parents[1]

class PruebasAplicacion(unittest.TestCase):
    def test_existe_archivo_principal(self):
        self.assertTrue((RAIZ / "index.html").is_file())

    def test_html_tiene_titulo_y_formulario(self):
        contenido = (RAIZ / "index.html").read_text(encoding="utf-8")
        self.assertIn("<title>Gestión Escolar", contenido)
        self.assertIn('id="form-estudiante"', contenido)

    def test_html_carga_css_y_javascript(self):
        contenido = (RAIZ / "index.html").read_text(encoding="utf-8")
        self.assertIn('href="styles.css"', contenido)
        self.assertIn('src="app.js"', contenido)

    def test_archivos_de_recursos_existen(self):
        self.assertTrue((RAIZ / "styles.css").is_file())
        self.assertTrue((RAIZ / "app.js").is_file())

if __name__ == "__main__":
    unittest.main()
