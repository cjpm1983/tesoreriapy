from django.contrib import admin
from .models import Iglesias, Obreros, Aportesiglesias, Aportesobreros
# Register your models here.


class IglesiasAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['iglesia']

class ObrerosAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['nombre']

class AportesiglesiasAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id','iglesia_id__iglesia','anio_id__anio']
    list_filter = ('iglesia_id','anio_id')
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('id','iglesia_id','anio_id')
        return self.readonly_fields

class AportesobrerosAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ['id','obrero_id__nombre','anio_id__anio']
    list_filter = ('obrero_id','anio_id')

admin.site.register(Iglesias,IglesiasAdmin)
admin.site.register(Obreros)
admin.site.register(Aportesiglesias,AportesiglesiasAdmin)
admin.site.register(Aportesobreros,AportesobrerosAdmin)


