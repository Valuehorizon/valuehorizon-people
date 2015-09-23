from django.contrib import admin
from people.models import Person
from countries.models import Country


class PersonAdmin(admin.ModelAdmin):
    search_fields=["first_name", "last_name",]
    filter_horizontal = ['nationalities']

    
admin.site.register(Person, PersonAdmin)
