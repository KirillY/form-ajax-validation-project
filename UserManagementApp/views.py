from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import auth
from django.http import Http404, HttpResponse
from UserManagementApp.forms import MyRegistrationForm
from django.contrib.auth.models import User
from UserManagementApp.models import UserLoginDatetime
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist


def update_user_last_login_datetime(request):
    event = UserLoginDatetime()  # creating an empty instance
    event.user_name = request.user.get_username()  # remember username in the attribute
    event.user_login_datetime = request.user.last_login
    event.save()
    return True


def login(request):
    if request.method == 'POST':
        # print("POST data =", request.POST)  # data in the 'request' object is placed in the POST attribute (dictionary)
        username = request.POST.get('login')  # from this "request" instance take POST attribute and get login
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)  # auth.authenticate returns User object or None
        # print('login -> user =', user)
        # print('last login time', user.last_login)
        if user:
            auth.login(request, user)  # logging user in
            update_user_last_login_datetime(request)
            return HttpResponseRedirect('/user/stats/')  # if we doesn't need a context
            # return login_stats(request)
            # both returns lead to main view with index.html template
            # but giving the GET method login form isn't shown
            # login view only accept POST methods
            # because of that we show form only when user is not authenticated

        else:  # if user is None, ie. user was not authenticated
            return render(request, 'index.html',
                          {'username': username, 'errors': True})  # errors:True - print 'login or pw doesn't exist'

            # return HttpResponseRedirect("/", {'errors': True}) #it's not possible to pass any arguments than path ('/') to HttpResponseRedirect
    raise Http404

def check_nickname(request):
    '''
    check if username (nickname) is available in existing database
    :param request: AJAX request
    :return: "true" in the response body if username is available, "false" otherwise
    '''
    # print(request.GET)
    if request.is_ajax():
        is_available = "false"
        if request.is_ajax():
            username = request.POST.get("username") # get username from the request QueryDict
            try:
                User.objects.get_by_natural_key(username)
            except ObjectDoesNotExist: # import ObjectDoesNotExist
                is_available = "true"
        return HttpResponse(is_available)
    raise Http404

def check_email(request):
    '''
    check if email is available in existing database
    :param request: AJAX request
    :return: "true" in the response body if email is available, "false" otherwise
    '''
    # print(request.GET)
    if request.is_ajax():
        is_available = "false"
        if request.is_ajax():
            email = request.POST.get("email") # get email from the request QueryDict
            try:
                # User.objects.get_by_natural_key(email)
                User.objects.get(email=email)
            except ObjectDoesNotExist: # import ObjectDoesNotExist
                is_available = "true"
        return HttpResponse(is_available)
    raise Http404

@user_passes_test(lambda u: u.is_authenticated)
def user_stats(request):
    user_login_data = UserLoginDatetime.objects.filter(user_name=request.user)
    return render(request, 'user_stats.html', {'user_login_data': user_login_data})


def logout(request):
    auth.logout(request)
    return render(request, "logout.html")

def reg_complete(request):
    return render(request, "reg_complete.html")

def registration(request):
    if request.method == 'POST':  # if user POST from the registration page
        form = MyRegistrationForm(request.POST) # create form object with arguments came from POST
        print(request.POST)
        if form.is_valid():
            form.save() # put form data into database
            # return HttpResponseRedirect('/') # render index.html
            return HttpResponseRedirect('/user/reg_complete/')
        context = {'form': form} # create context with form data and errors
        return render(request, 'registration.html', context)  # render data and errors on the page
    context = {'form': MyRegistrationForm()} # if user request registration form page first time with GET request
    return render(request, 'registration.html', context) # return template with a form without arguments


# def create_user(request, user_id=None):
#     """
#     Создает Пользователя(User)
#     Или редактирует существующего, если указан  user_id
#     """
#     if request.is_ajax():
#         print('user_id = ', user_id)
#         if not user_id:
#             print('Not user_id')
#             user = User(request.POST)
#         else:
#             user = get_object_or_404(User, id=user_id)
#             user = UserChangeForm(request.POST or None, instance=user)
#         if user.is_valid():
#             user.save()
#             users = User.objects.all()
#             html = loader.render_to_string('inc-users_list.html', {'users': users}, request=request)
#             data = {'errors': False, 'html': html}
#             return JsonResponse(data)
#         else:
#             errors = user.errors.as_json()
#             return JsonResponse({'errors': errors})
#
#     raise Http404

@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    users = User.objects.all()
    return render(request, 'admin-page.html', {'users': users})


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')
