from django.db import models
from django.contrib.auth.models import User


# This polls can be answered by registered users only, so there is no need for random hash cookies and user_agent info
# Questions can have text answer or bullet list (with one option only)

### SURVEY section ###
# survey is a combination of questions in the given order (without any responses)
# each question can consist of several options

class Survey(models.Model):
    survey_name = models.CharField(verbose_name='Survey name', max_length=100)
    survey_description = models.CharField(verbose_name='Survey description', max_length=1000, blank=True)
    survey_update = models.DateTimeField(verbose_name='Survey last update datetime')


class Question(models.Model):
    question_text = models.CharField(verbose_name='Question text', max_length=300)
    question_update = models.DateTimeField(verbose_name='Survey last update datetime')


class QuestionOrder(models.Model):
    question_id = models.ForeignKey(Question)
    survey_id = models.ForeignKey(Survey)
    order_number = models.IntegerField(verbose_name='Question number in the survey')


class QuestionOptions(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(verbose_name='Option text', max_length=100)


### ANSWERS section ###
# responses consist of UserSurvey instances which represent User--Survey many-to-many relationships ie.
# User can take part in many surveys and one Survey can be used by many Users;
# each UserSurvey instance consists of many Answer instances,
# which represent UserSurvey--Question many-to-many relationships ie.
# one Question can be used in many UserSurveys and one UserSurvey consists of many questions


class UserSurvey(models.Model):
    survey_id = models.ForeignKey(Survey)
    user_id = models.ForeignKey(User)
    response_update = models.DateTimeField(verbose_name='User survey response update datetime')


class Answer(models.Model):
    user_survey_id = models.ForeignKey(UserSurvey)
    question_id = models.ForeignKey(Question)
    text_answer = models.CharField(verbose_name='Text answer', max_length=300)
    option_id = models.ForeignKey(QuestionOptions) # !all questions are limited by 1 option
    user_id = models.ForeignKey(User)
