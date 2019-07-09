from django.contrib import admin

from .models import Tongue, Body, Person, Cases, Yao, Xue

admin.site.register(Person)
admin.site.register(Tongue)
admin.site.register(Body)
admin.site.register(Cases)
admin.site.register(Yao)
admin.site.register(Xue)

