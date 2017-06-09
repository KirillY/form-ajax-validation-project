////var csrftoken = $.cookie('csrftoken');
//var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
//
//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
//
//$.ajaxSetup({
//    beforeSend: function(xhr, settings) {
//        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//            xhr.setRequestHeader("X-CSRFToken", csrftoken);
//        }
//    }
//});

// true if first symbol is a-z or A-Z letter
jQuery.validator.addMethod("rulettersonly", function(value, element) {
  return this.optional(element) || /^[а-я]+$/i.test(value);
}, "Letters only please");

// true if first symbol is a-z or A-Z letter and other symbols are letters or numbers
jQuery.validator.addMethod("letterfirstonly", function(value, element) {
  return this.optional(element) || /^[a-z]\w*$/i.test(value);
}, "First symbol letter only please");

$(document).ready(function() {
    $('#user-form').validate({ //address to user-form
    rules: {
         username: {
             required: true,
             letterfirstonly: true
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
             email: true
         },
         password1: {
             minlength: 5
         }
     },
     messages: {
         username: {
             required: "Необходимо ввести никнейм",
             letterfirstonly: "Никнейм должен начинаться с буквы, остальные символы - буквы или цифры"
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
              email: "Введите корректный e-mail"
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