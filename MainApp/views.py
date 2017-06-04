from django.shortcuts import render
# from MainApp.models import UserLoginDatetime


def main(request):
    return render(request, 'index.html')


# def login_stats(request):
#     user_login_data = UserLoginDatetime.objects.filter(user_name=request.user)
#     return render(request, 'login_stats.html', {'user_login_data':user_login_data})
