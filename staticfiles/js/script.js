// Ejemplo de un script simple
document.addEventListener('DOMContentLoaded', function() {
    console.log("¡El sitio está listo!");
});

document.querySelectorAll('.estrellas-calificacion label').forEach(label => {
    label.addEventListener('click', function() {
        const estrellas = Array.from(document.querySelectorAll('.estrellas-calificacion label'));
        estrellas.forEach(star => star.style.color = '#ddd');
        let index = estrellas.indexOf(this);
        for (let i = 0; i <= index; i++) {
            estrellas[i].style.color = '#ffc107';
        }
    });
});

// scripts.js

// Seleccionar el botón para abrir el modal
const openModalBtn = document.getElementById('openModalBtn');
// Seleccionar el modal
const modal = document.getElementById('modal');
// Seleccionar el botón de cancelar
const cancelBtn = document.getElementById('cancelBtn');

// Función para abrir el modal
openModalBtn.addEventListener('click', function() {
    modal.style.display = 'block';
});

// Función para cerrar el modal
cancelBtn.addEventListener('click', function() {
    modal.style.display = 'none';
});

// Si se hace clic fuera del modal, también cerrarlo
window.addEventListener('click', function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});
console.log("scripts.js cargado correctamente.");
