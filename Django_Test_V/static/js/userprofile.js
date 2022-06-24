
let navbar = document.querySelector('.navbar')

document.querySelector('#menu_btn').onclick = () =>{
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
    searchForm.classList.remove('active');
}

let userprofile = document.querySelector('.User-Profile')

document.querySelector('#User-Profile').onclick = () =>{
    userprofile.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

var swiper = new Swiper(".product-slider", {
    loop:true, 
    grabCursor:true,
    spaceBetween: 20,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
          slidesPerView: 1,
        },
        640: {
          slidesPerView: 2,
        },
        768: {
          slidesPerView: 3,
        },
        1024: {
          slidesPerView: 4,
        },
    },
});