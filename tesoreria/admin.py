from django.contrib import admin
from .models import Iglesias, Obreros, Aportesiglesias, Aportesobreros

from django.utils.html import format_html
from django.urls import reverse, path
# Register your models here.

admin.site.site_header = "Tesorería Buenas Nuevas"


from . import views


admin.site.register_view('estadistica',visible=True,name="Reportes",urlname='estadistica',view=views.estadistica)



class IglesiasAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('iglesia', 'provincia','presbiterio','aportes','activa')
    ordering = ('presbiterio','provincia','iglesia')
    fieldsets = (
        (None, {'fields': ('iglesia', 'provincia','presbiterio','activa')}),
        ('Obreros', {'fields': ('misioneros',)}),
        ('Fechas', {'fields': ('alta','baja')})
    )
    list_filter = ['presbiterio','provincia']

    def aportes(self, obj):
        link = '/admin/tesoreria/aportesiglesias/?iglesia_id__id__exact=%d' % obj.id  # 'admin:tesoreria_aportesobreros_change')
        return format_html('<a href="{}">{}</a>', link,
                           '%d Aportes' % Aportesiglesias.objects.filter(iglesia_id=obj.id).count())

    search_fields = ['iglesia']
    filter_horizontal = ['misioneros']


class ObrerosAdmin(admin.ModelAdmin):
    #exclude = ['alta','baja']
    list_per_page = 12
    search_fields = ['nombre','iglesia_id__iglesia']
    filter_horizontal = ['iglesia_id']
    list_display = ('nombre','aportes','folio','activo')
    ordering = ('nombre',)

    # list_display = ('aportes',)
    def aportes(self,obj):
         link = '/admin/tesoreria/aportesobreros/?obrero_id__id__exact=%d' % obj.id #'admin:tesoreria_aportesobreros_change')
         return format_html('<a href="{}">{}</a>', link, '%d Aportes' % Aportesobreros.objects.filter(obrero_id=obj.id).count())


class AportesiglesiasAdmin(admin.ModelAdmin):
    list_per_page = 12
    search_fields = ['id','iglesia_id__iglesia','anio_id__anio']
    list_filter = ('iglesia_id','anio_id')
    fieldsets = (
        (None, {'fields': ('iglesia_id', 'anio_id')}),
        ('Desglose mensual', {'fields': ('ene', 'feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'),'classes': ['collapse']}),
    )

    list_display = ('iglesia_id','anio_id',"total")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id','iglesia_id','anio_id','total')
        return self.readonly_fields

    ordering = ('iglesia_id__iglesia','anio_id__anio')


class AportesobrerosAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['id','obrero_id__nombre','anio_id__anio']
    list_filter = ('anio_id',)

    fieldsets = (
        (None, {'fields': ('obrero_id', 'anio_id')}),
        ('Desglose mensual', {'fields': ('ene', 'feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'),'classes': ['collapse']}),
    )

    list_display = ('obrero_id','anio_id',"total")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id','obrero_id','anio_id','total')
        return self.readonly_fields

    ordering = ('obrero_id__nombre','anio_id__anio')

    ordering = ('obrero_id__nombre', 'anio_id__anio')

admin.site.register(Iglesias,IglesiasAdmin,)
admin.site.register(Obreros,ObrerosAdmin)
admin.site.register(Aportesiglesias,AportesiglesiasAdmin)
admin.site.register(Aportesobreros,AportesobrerosAdmin)



