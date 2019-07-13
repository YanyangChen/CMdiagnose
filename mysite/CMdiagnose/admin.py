from django.contrib import admin

from .models import Tongue, Body, Person, Cases, Yao, Xue
# https://stackoverflow.com/questions/28512710/how-to-add-custom-search-box-in-django-admin
class CasesAdmin(admin.ModelAdmin):

    list_display=('pk','solution','symptom','facts')
    search_fields = ('solution', 'symptom', 'facts')
admin.site.register(Person)
admin.site.register(Tongue)
admin.site.register(Body)
# admin.site.register(Cases)
admin.site.register(Yao)
admin.site.register(Xue)
admin.site.register(Cases, CasesAdmin)



