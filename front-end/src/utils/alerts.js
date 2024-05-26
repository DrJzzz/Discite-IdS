import Swal from "sweetalert2";

export function alertSuccess(message){
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        iconColor: '#43cc29',
        toast: true,
        text: message,
        background: '#7b8ab8',
        color : '#1e4c2e',
        showConfirmButton: false,
        timer: 2000
    });
}

export function alertError(message){
    Swal.fire({
        position: 'top-end',
        icon: 'error',
        iconColor: '#d9534f',
        toast: true,
        showConfirmButton: false,
        text: message,
        color: '#572120',
        background: '#7b8ab8',
        timer: 2000
    });
}