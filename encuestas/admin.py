from django.contrib import admin
from .models import Question, UserProfile
from .models import Choice
from .models import Persona
from .models import Curso
from .models import Calificacion


# Register your models here.
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    '''


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['question_text', 'pub_date']
    search_fields = ['question_text', 'pub_date']

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    pass





admin.site.register(Question, QuestionAdmin)

