Django 1.11.1
Python 3.6.1

su login: django
password: geekbrains
Админка: /admin/ 

---
*ТЕХНИЧЕСКОЕ ЗАДАНИЕ*

Запрограммировать страницу регистрации.

Запрограммированная страница должна выглядеть так же, как на макете.

Создать БД MySQL с единственной таблицей users.

Поля должны проверяться как на стороне клиента, так и на стороне сервера.
При вводе некорректного значения рядом с полем выводится "восклицательный знак" и сообщение об ошибке.
После ввода корректного значения рядом с полем выводится "галочка", сообщение об ошибке исчезает.

- Никнэйм:
  Должен содержать только латинские буквы и цифры, начинаться должен с латинской буквы.
  Заглавные и прописные символы не различаются, сохранятется в том регистре, в котором был введен.
  Проверяется на существование (в БД) без обновления страницы.

- Имя
  Допустимы только русские буквы.
 
- Фамилия
  Допустимы только русские буквы.
  
- Электронная почта
  Введенное значение должно быть корректным адресом e-mail
  Проверяется на существование (в БД) без обновления страницы.

- Пароль
  Не меньше 5 произвольных символов.

Кнопка "Готово" становится доступной только после того, как все поля заполнены корректно.
Если после этого в поля формы вводится некорректное значение кнопка снова становится неактивной.

После отправки формы данные сохраняются в БД, выдается страница с текстом "Регистрация завершена."
   
---
*РЕАЛИЗАЦИЯ* 

Стартовые условия: 
    Стартовый URL с формой /user/registration/ либо выбрать в меню "Registration"
    Использован jQuery validation plugin, для AJAX запросов использован встроенный в плагин метод remote
    Для удобства портирования на стадии разработки использована БД SQLite, при необходимости в Settings переключается на MySQL (2 строки кода)

Структура проекта: 
    Использованы встроенные формы UserCreationForm, немного видоизмененные в UserManagementApp/forms.py
    Основная логика валидации находится в static/js/user_registration_validation.js и UserManagementApp/views.py
    Обработчик запросов - Tools/urls.py; Поля формы - UserManagementApp/forms.py; Шаблоны - templates/included-reg-form.html, templates/registration.html

Опции и фичи: 
    Валидация на стороне клиента - соответствие регулярному выражению (согласно заданию) для полей: символы никнейма, имени, фамилии, корректность адреса почты, количество символов пароля
    Валидация на стороне сервера - доступность никнейма и почты для регистрации
    Оставил внутреннюю валидацию Django (на стороне сервера) - на случай, если не загрузится JS () -- views.py form.is_valid()
    Для предупреждения межсайтового скриптинга  AJAX-запросы к серверу передаются методом POST с использование csrftoken 
    Можно пользоваться формой, если у пользователя не загружен JavaScript (disabled property выставляется внутри js скрипта)
    Имя и фамилия не обязательные поля
    Подсказки в формах
    "Ленивая" валидация - пока пользователь не ввел значение в форму не отображается сообщение об ошибке
    Кнопка "Готово" не активна пока форма не пройдет валидацию
    Список пользователей можно посмотреть, если залогиниться под su login (см. в начале описания), далее зайти на /admin/
    
