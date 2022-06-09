// const body = document.querySelector('body');
// const modal = document.querySelector('.modal');
// // const btnOpenPopup = document.querySelectorAll('.btn-open-popup');
// // const btnOpenPopup = document.getElementsByClassName("btn-open-popup");
// const cancel_btn = document.querySelector('.cancel_btn');
// const funcs = [];
//
// // console.log(btnOpenPopup);
// document.querySelectorAll('.btn-open-popup').forEach((cell) => {
//     cell.addEventListener('click', function () {
//         modal.classList.toggle('show');
//         if (modal.classList.contains('show')) {
//             body.style.overflow = 'hidden';
//         }
//     });
// });
//
// cancel_btn.addEventListener('click', () => {
//     modal.classList.toggle('show');
//     if (!modal.classList.contains('show')) {
//         body.style.overflow = 'auto';
//     }
// });
//
// modal.addEventListener('click', (event) => {
//     if (event.target === modal) {
//         modal.classList.toggle('show');
//
//         if (!modal.classList.contains('show')) {
//             body.style.overflow = 'auto';
//         }
//     }
// });
const modal = document.getElementById('modal_open');
$(function(){

    $("button[id='close_modal']").click(function(){
        $("div[id = 'modal_open']").fadeOut();
        document.body.style.overflowY = 'show';
    });

});
 window.onload = function()
{

    const body = document.querySelector('body');
    // const modal = document.querySelector('.modal');

    const modal = document.getElementsByClassName('modal');

    const btnOpenPopup = document.querySelectorAll('.btn-open-popup');

    const btnOpenPopup1 = document.getElementById('btn1');
    const btnOpenPopup2 = document.getElementById('btn2');

    // const btnOpenPopup = document.getElementsByClassName("btn-open-popup");
    const cancel_btn = document.querySelector('.cancel_btn');
    const delete_btn = document.querySelector('.delete_btn');
    // const funcs = [];


    console.log(btnOpenPopup);

    let funcs = [];

    // Modal을 띄우고 닫는 클릭 이벤트를 정의한 함수
    function Modal(num) {
        return function() {
        // 해당 클래스의 내용을 클릭하면 Modal을 띄웁니다.
            btnOpenPopup[num].onclick =  function() {
                modal[num].style.display = "block";
                console.log(num);
            };

            // (X 버튼)를 클릭하면 Modal 닫기
            // spanes[num].onclick = function() {
            //     modals[num].style.display = "none";
            // };
        };
    }



    for(let i = 0; i < btnOpenPopup.length; i++) {
        funcs[i] = Modal(i);
    }

    // 원하는 Modal 수만큼 funcs 함수를 호출합니다.
    for(let j = 0; j < btnOpenPopup.length; j++) {
        funcs[j]();
    }

}
