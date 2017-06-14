// # Using jQuery validation plugin #
// Source: http://ajax.aspnetcdn.com/ajax/jquery.validate/1.11.1/jquery.validate.min.js

// ### Additional validation methods ###
// true if first symbol is a-z or A-Z letter
jQuery.validator.addMethod("rulettersonly", function(value, element) {
  return this.optional(element) || /^[а-я]+$/i.test(value);
}, "Letters only please");

// true if first symbol is a-z or A-Z letter and other symbols are letters or numbers
jQuery.validator.addMethod("letterfirstonly", function(value, element) {
  return this.optional(element) || /^[a-z]\w*$/i.test(value);
}, "First symbol letter only please");

// ### Validation rules ###
$(document).ready(function() {
    $('#user-form').validate({ //address to #user-form in registration.html
    rules: {
         username: {
             required: true,
             letterfirstonly: true,
             remote: {
                url:"/user/check_nickname/",
                type:"post", // GET method is used by default
                data: { // form data is sent by default, but we need to specify csrf, reassigning the username
                    csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    username: function() { return $( "#id_username" ).val(); }
                    }
            }
         },
         first_name: {
             required: false,
             rulettersonly: true
         },
         last_name: {
             required: false,
             rulettersonly: true
         },
         email: {
             required: true,
             email: true,
             remote: {
                url:"/user/check_email/",
                type:"post",
                data: {
                    csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    email: function() { return $( "#id_email" ).val(); }
                    }
            }
         },
         password1: {
             minlength: 5
         }
     },
    messages: {
         username: {
             required: "Необходимо ввести никнейм",
//             required: "",
             letterfirstonly: "Никнейм должен начинаться с буквы, остальные символы - буквы или цифры",
             remote: "Человек с таким никнеймом уже зарегистрирован"
         },
         first_name: {
             required: false,
             rulettersonly: "Необходимо использовать только буквы русского алфавита"
         },
         last_name: {
             required: false,
             rulettersonly: "Необходимо использовать только буквы русского алфавита"
         },
         email: {
              required: "Необходимо ввести email",
//              required: "",
              email: "Введите корректный e-mail",
              remote: "Человек с таким электронным адресом уже зарегистрирован"
         },
         password1: {
             required: "Необходимо ввести пароль",
//             required: "",
             minlength: "Пожалуйста, выдумайте пароль длиннее 5 символов"
         },
         success: function(label) {
             label.addClass("valid").text("Ok!")
         },
         errorPlacement: function(error) {
             $("#response").html(error);
            }
     },
     onkeyup: true
//     debug: true

    });
// hiding button
//    $('button.btn').prop('disabled', 'disabled');
// basic script to hide submit button
//    $('#user-form input').on('blur', function () { // fires on every keyup & blur
//        if ($('#user-form input').valid()) {                   // checks form for validity
//            $('button.btn').prop('disabled', false);        // enables button
//        } else {
//            $('button.btn').prop('disabled', 'disabled');   // disables button
//        }
//    });

// disable submit button !with one side effect - cancelling 'lazy typing'
//    $('#user-form input').on('keyup', function () { // fires on every keyup & blur & focus
////        if ($("input").each(hasClass("error"))) {                   // checks form for validity
//        if ( $("input.error").length > 0 ) { // side effect - stay valid if empty forms exists
////        if ( $("input.error").length > 0 || !$("input[required]").valid() ) {
////        if ( !$("input[required]").valid() ) { // works! but with side effect - show next error
//            $('button.btn').prop('disabled', 'disabled');   // disables button
//        } else {
////            alert('Valid form')
//            $('button.btn').prop('disabled', false);        // enables button
//        }
//    });

// works fine except sometimes hide submit after password enter
//    $('#user-form input').on('keyup', function () {
//        $('input[required]').each(function() {
//            if ($("input.error").length > 0 || !$(this).val()) {
//                $('button.btn').prop('disabled', 'disabled');   // disables button
//            } else {
////            alert('Valid form')
//                $('button.btn').prop('disabled', false);        // enables button
//                }
//            })
//    });

});