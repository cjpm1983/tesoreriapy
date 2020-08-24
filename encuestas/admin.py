from django.contrib import admin
from .models import Question, UserProfile
from .models import Choice
from .models import Persona
from .models import Curso
from .models import Calificacion
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from django.utils.html import format_html



# Register your models here.
'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
    '''


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ('username', 'is_staff', 'is_active')
    list_filter = ('username', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal_Data', {'fields': ('email', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('groups', 'is_staff', 'is_active', 'is_superuser')}),
        ('Images', {'fields': ('avatar', 'background')}),
        # ('Dates', {'fields': ('last_login', 'date_joined')}),

        # ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    # add_fieldsets = (
    #     (None,{
    #         'classes':('wide',),
    #         'fields':('username','password1','password2','is_staff','is_active')
    #     })
    # )
    search_fields = ('username',)
    ordering = ('username',)


# @admin.register()
# class ChoiceInline(admin.StackedInline):
#    model = Choice
#    extra = 3

#
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     # inlines = [ChoiceInline]
#     list_display = ('question_text', 'pub_date')
#     list_filter = ['question_text', 'pub_date']
#     search_fields = ['question_text', 'pub_date']
#
#
# @admin.register(Persona)
# class PersonaAdmin(admin.ModelAdmin):
#     list_per_page = 10
#     search_fields = ['first_name', 'last_name']
#
#
# @admin.register(Curso)
# class CursoAdmin(admin.ModelAdmin):
#     list_display = ('compuesto', 'name', 'year', 'activo')
#     list_filter = ['activo', 'year']
#     filter_horizontal = ['personas']
#
#     def activo_html_display(self, obj):
#         respuesta = 'No'
#         if obj: respuesta = "Si"
#
#         return format_html(
#             f'<span >{respuesta}</span>'
#         )
#
#
# @admin.register(Calificacion)
# class CalificacionAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Question, QuestionAdmin)
