// 모달 열기
// const modal = document.getElementById('modal_open');
// const buttonAddFeed = document.getElementById('modal_btn');
// const modal = document.querySelector('div[class="modal_overlay"]');
// const buttonAddFeed = document.querySelector('button[class="card__description"]');
// buttonAddFeed.addEventListener('click', e => {
//     modal.style.display = 'flex';
//     document.body.style.overflowY = 'hidden'; // 스크롤 없애기
// });
// const elements1 = document.querySelectorAll('[name="box1"]');
//
// const el1 = document.querySelector('div[name="bo"]');
//
// document.querySelector('#foobar[name="bo"]');
//
// document.querySelector('.modal[name="bo"]');
// 모달 닫기
// const buttonCloseModal = document.getElementById('close_modal');
// buttonCloseModal.addEventListener('click', e => {
//     modal.style.display = 'none';
//     document.body.style.overflowY = 'visible';
// });
const modal = document.getElementById('modal_open');
$(function(){

    $("button[id='modal_btn']").click(function(){
        $("div[id = 'modal_open']").fadeIn();
        modal.style.display = 'flex';
        document.body.style.overflowY = 'hidden';
    });

    $("button[id='close_modal']").click(function(){
        $("div[id = 'modal_open']").fadeOut();
        document.body.style.overflowY = 'show';
    });

});