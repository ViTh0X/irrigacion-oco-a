document.addEventListener("DOMContentLoaded", function() {
    const nav = document.querySelector('.opciones_menu');
    const enlaces = nav.querySelectorAll('a');
    const primerEnlace = enlaces[0];
    const ultimoEnlace = enlaces[enlaces.length - 1];

    nav.addEventListener('keydown', function(e) {
        // Solo nos interesa la tecla Tab
        if (e.key === 'Tab') {
            
            // Si presiona Shift + Tab (Retroceder) y está en el primero
            if (e.shiftKey) {
                if (document.activeElement === primerEnlace) {
                    e.preventDefault();
                    ultimoEnlace.focus();
                }
            } 
            // Si presiona Tab (Avanzar) y está en el último
            else {
                if (document.activeElement === ultimoEnlace) {
                    e.preventDefault();
                    primerEnlace.focus();
                }
            }
        }
    });
});
