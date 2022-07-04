let navbar = document.querySelector('.navbar')

document.querySelector('#menu_btn').onclick = () => {
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
    searchForm.classList.remove('active');
}

let userprofile = document.querySelector('.User-Profile')

document.querySelector('#User-Profile').onclick = () => {
    userprofile.classList.toggle('active');
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}

$('.form-control').each(function() {
    floatedLabel($(this));
});

$('.form-control').on('input', function() {
    floatedLabel($(this));
});

function floatedLabel(input) {
    var $field = input.closest('.form-group');
    if (input.val()) {
        $field.addClass('input-not-empty');
    } else {
        $field.removeClass('input-not-empty');
    }
}