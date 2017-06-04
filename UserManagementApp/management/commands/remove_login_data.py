from django.core.management.base import BaseCommand, CommandError
from UserManagementApp.models import UserLoginDatetime
from datetime import datetime, timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Delete user login data older than a given amount of seconds, 7884000 sec or 3 months by default'

    def add_arguments(self, parser):
        parser.add_argument('seconds', nargs='?', type=int, default=7884000)

    def handle(self, *args, **options):
        interval = options['seconds']

        threshold_date = timezone.now() - timedelta(seconds=interval)  # use timezone to escape RuntimeWarning
        login_data = UserLoginDatetime.objects.filter(user_login_datetime__lt=threshold_date)  # lt = less_than
        if login_data:
            counter = 0
            # print(login_data is None)
            for login_event in login_data:
                login_event.delete()
                counter += 1
            self.stdout.write(self.style.SUCCESS('Successfully delete {} login events'.format(counter)))
        else:
            self.stdout.write('Error: no login data older than {}'.format(threshold_date))

# schtasks /Create /TN djangologin /TR "C:\Users\Cactus\.virtualenvs\djangodev\Scripts\python.exe C:\Users\Cactus\OneDrive\Работа\Neswrucom\quiz-probation-project\manage.py \"remove_login_data\" \"1\""