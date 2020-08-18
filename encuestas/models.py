from django.db import models
from django import template

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .managers import UserProfileManager


# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    #user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="encuestas/avatars", null=True, blank=True, default='static/assets/img/theme/team-1-800x800.jpg')
    background = models.ImageField(upload_to="encuestas/avatars_bg", null=True, blank=True, default='static/assets/img/theme/profile-cover.jpg')

    #objects = UserProfileManager

    def __str__(self):
        return self.username


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    #question_type = models.CharField(max_length=200, verbose_name='tipo de pregunta', default='simple_select')
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Persona(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Curso", blank = True)

    class Meta:
        verbose_name_plural = "Personas"

class Curso(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name","year",)

class Calificacion(models.Model):
    persona = models.ForeignKey(Persona, on_delete = models.CASCADE)
    calificacion = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)