function bienvenida() {
    console.log("Página cargada correctamente"); /* muestra este mensaje en la consola */
}

function saludar() {
    alert("¡Hola, mundo!"); /* la función alert abre un modal con el mensaje que le enviemos enetre paréntesis */
}

function mostrarSeleccion(valor) {
    document.getElementById("resultadoFruta").innerText = "Elegiste: " + valor; /* obtenermos el elemento con id resultadoFruta, innerText inyecta ese textto en el ID seleccionado */
}

/* e es el objeto de evento que el navegador le pasa automáticamente a su función (memorizar eso) cuando la usan como manejador de eventos. Se puede llamar e, event, ev, como quieran: es el parámetro que representa “lo que ocurrió” (tipo de evento, tecla, elemento objetivo, etc.). */

/* e.key → la tecla según el carácter lógico ("a", "Enter", "ArrowLeft", etc.).

Otros útiles:

e.code → la tecla física del teclado ("KeyA", "Enter", etc.).

e.type → tipo de evento ("keydown", "keyup", …).

e.target → el elemento que disparó el evento.

e.preventDefault() → cancelar el comportamiento por defecto.

e.stopPropagation() → detener la propagación (bubbling). */

function detectarTecla(e) {
    console.log("Presionaste la tecla: " + e.key);
}

function validarFormulario() {
    const nombre = document.getElementById("nombre").value;
    if (nombre.trim() === "") { /* trim quita espacios en blanco alrededor, es para limpiar */
        alert("Por favor ingresa tu nombre");
        return false;
    }
    
    alert("Formulario enviado con éxito");
    return true;
}

document.getElementById("botonModerno").addEventListener("click", function() {
    alert("¡Usando addEventListener!");
});