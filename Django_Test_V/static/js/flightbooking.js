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


