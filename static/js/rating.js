//모달 html div id 를 변수에 저장
const modal = document.getElementById('modal_open');

// 모달 창 열기 // onclick 으로 openModal() 함수 실행하며 받은 인자들 ( django views에서 받은 값들이 들어있다.)
function openModal(url,name,style,category,aroma,flavor,balance,season,body) {

    // class명으로 쓰는 이유는 여러개의 모달이 존재해서 하나의 id로 열 수 없기 때문
    $(".modal_overlay").fadeIn();
    // 모달의 display 속성 변경해주기
    modal.style.display = 'flex';
    // 모달 열리면서 스크롤 막기
    document.body.style.overflowY = 'hidden';

    //팝업창을 가운데로 띄우기 위해 현재 화면의 가운데 값과 스크롤 값을 계산하여 팝업창 CSS 설정
    $(".modal_overlay").css({
        "top": (($(window).height()-$(".modal_overlay").outerHeight())/2+$(window).scrollTop())+"px",
        "left": (($(window).width(2000)-$(".modal_overlay").outerWidth())/2+$(window).scrollLeft())+"px"
     });

    // 이미지 변경 : `{% static ${url} %}` 사용하면 html에서 받을때 절대경로로 /rating/이 자동으로 붙어 가져올수없음
    // 상대 경로 ../ 사용
    document.getElementById('beer_img').src = `../static/${url}`;

    // 모달 텍스트 변경
    document.getElementById('beer_name').textContent = name;
    document.getElementById('beer_style').textContent = style;
    document.getElementById('beer_category').textContent = category;
    document.getElementById('beer_aroma').textContent = aroma;
    document.getElementById('beer_flavor').textContent = flavor;
    document.getElementById('beer_balance').textContent = balance;
    document.getElementById('beer_season').textContent = season;
    document.getElementById('beer_body').textContent = body;
    // beer_info = document.getElementById('modal_info').textContent=name;
    // beer_id = document.createTextNode(id);
    // beer_info.appendChild(beer_id);

}

$(function(){
    // 모달 창 열기
    // $("#modal_btn").click(function(){
    //     $("div[id = 'modal_open']").fadeIn();
    //     modal.style.display = 'flex';
    //     document.body.style.overflowY = 'hidden';
    // });


    // 모달 창 닫기(닫기버튼)
    $("button[id='close_modal']").click(function(){
        $("div[id = 'modal_open']").fadeOut();
        document.body.style.overflowY = 'scroll';
    });
    // 모달 창 닫기(영역밖 클릭)
    $(document).on("click", function(e){
        if( $("#modal_open").is(e.target)) {
        $("div[id = 'modal_open']").fadeOut();
        document.body.style.overflowY = 'scroll';
    }
    });
});




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
