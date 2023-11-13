const rows = document.querySelectorAll('tr');

rows.forEach((row) => {
    row.addEventListener('click', (event) => {
        event.stopPropagation(); // Evita que el evento se propague a elementos superiores

        // Si la fila no tiene la clase 'title-row', aplica la lógica de selección
        if (!row.classList.contains('fila__titulo')) {
            // Remueve la clase 'selected' de todas las filas
            rows.forEach((r) => {
                r.classList.remove('selected');
            });

            // Agrega la clase 'selected' a la fila clicada
            row.classList.add('selected');
        }
    });
});

document.addEventListener('click', (event) => {
    // Si el clic no fue en una fila, elimina la clase 'selected' de todas las filas
    if (!event.target.closest('tr')) {
        rows.forEach((row) => {
            row.classList.remove('selected');
        });
    }
});
