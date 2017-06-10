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
             remote: "/user/check_nickname/"
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
             remote: "/user/check_email/"
         },
         password1: {
             minlength: 5
         }
     },
     messages: {
         username: {
             required: "Необходимо ввести никнейм",
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
              email: "Введите корректный e-mail",
              remote: "Человек с таким электронным адресом уже зарегистрирован"
         },
         password1: {
             required: "Необходимо ввести пароль",
             minlength: "Пожалуйста, выдумайте пароль длиннее 5 символов"
         },
         success: function(label) {
             label.addClass("valid").text("Ok!")
         },
         errorPlacement: function(error) {
             $("#response").html(error);
         }
      }
    });
});