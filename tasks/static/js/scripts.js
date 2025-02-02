document.addEventListener('DOMContentLoaded', function() {
    console.log("¡El sitio está listo!");

    // Seleccionar el botón para abrir el modal
    const openModalBtn = document.getElementById('openModalBtn');
    // Seleccionar el modal
    const modal = document.getElementById('modalCompra');
    // Seleccionar el botón de cancelar
    const cancelBtn = document.getElementById('cancelarCompra');

    if (openModalBtn) {
        // Función para abrir el modal
        openModalBtn.addEventListener('click', function() {
            modal.style.display = 'block';
        });
    }

    if (cancelBtn) {
        // Función para cerrar el modal
        cancelBtn.addEventListener('click', function() {
            modal.style.display = 'none';
        });
    }

    // Si se hace clic fuera del modal, también cerrarlo
    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
    
    console.log("scripts.js cargado correctamente.");
});
