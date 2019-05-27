from django.contrib import admin

from .models import Tongue, Body, Person, Cases

admin.site.register(Person)
admin.site.register(Tongue)
admin.site.register(Body)
admin.site.register(Cases)

