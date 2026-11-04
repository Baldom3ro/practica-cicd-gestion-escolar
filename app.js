const formulario = document.getElementById("form-estudiante");
const lista = document.getElementById("lista-estudiantes");
const total = document.getElementById("total-estudiantes");
const mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", function (evento) {
  evento.preventDefault();
  const nombre = document.getElementById("nombre").value.trim();
  const matricula = document.getElementById("matricula").value.trim();

  if (!nombre || !matricula) {
    mensaje.textContent = "Captura el nombre y la matrícula.";
    return;
  }

  const fila = document.createElement("tr");
  const celdaMatricula = document.createElement("td");
  const celdaNombre = document.createElement("td");
  celdaMatricula.textContent = matricula;
  celdaNombre.textContent = nombre;
  fila.append(celdaMatricula, celdaNombre);
  lista.appendChild(fila);

  total.textContent = String(lista.rows.length);
  mensaje.textContent = "Estudiante agregado correctamente.";
  formulario.reset();
});
