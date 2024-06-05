// Función para convertir la fecha GMT a un formato legible
export function formatDate(gmtDate) {
    const date = new Date(gmtDate);
    return date.toLocaleString();
}