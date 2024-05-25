// src/utils/csrf.js

/**
 * Función para obtener el valor de una cookie por su nombre.
 * @param {string} name - Nombre de la cookie a obtener.
 * @returns {string|null} - Valor de la cookie o null si no se encuentra.
 */
export function getCookie(name) {
    if (typeof document === 'undefined') {
        return null;
    }

    let cookieValue = null;
    if (document.cookie) {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
