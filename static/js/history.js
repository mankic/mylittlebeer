const body = document.querySelector('body');
const modal = document.querySelector('.modal');
// const btnOpenPopup = document.querySelectorAll('.btn-open-popup');
// const btnOpenPopup = document.getElementsByClassName("btn-open-popup");
const cancel_btn = document.querySelector('.cancel_btn');
const funcs = [];

// console.log(btnOpenPopup);
document.querySelectorAll('.btn-open-popup').forEach((cell) => {
    cell.addEventListener('click', function () {
        modal.classList.toggle('show');
        if (modal.classList.contains('show')) {
            body.style.overflow = 'hidden';
        }
    });
});

cancel_btn.addEventListener('click', () => {
    modal.classList.toggle('show');
    if (!modal.classList.contains('show')) {
        body.style.overflow = 'auto';
    }
});

modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.classList.toggle('show');

        if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
        }
    }
});
