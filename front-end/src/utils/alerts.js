import Swal from "sweetalert2";
import {goto} from "$app/navigation";

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

export function alertEndStudy(message, icon){
    let timerInterval;
    Swal.fire({
        title: message,
        timer: 2000,
        icon: icon,
        timerProgressBar: true,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
            const timer = Swal.getPopup().querySelector("b");
            timerInterval = setInterval(() => {
                timer.textContent = `${Swal.getTimerLeft()}`;
            }, 100);
        },
        willClose: () => {
            clearInterval(timerInterval);
        }
    }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
        }
    });
}


export function alertCenter(message, icon){
    let timerInterval;
    Swal.fire({
        title: message,
        timer: 2000,
        icon: icon,
        showConfirmButton: false,
        didOpen: () => {
            Swal.showLoading();
            const timer = Swal.getPopup().querySelector("b");
            timerInterval = setInterval(() => {
                timer.textContent = `${Swal.getTimerLeft()}`;
            }, 100);
        },
        willClose: () => {
            clearInterval(timerInterval);
        }
    }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
        }
    });
}
