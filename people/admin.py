from django.contrib import admin
from people.models import Person
from countries.models import Country
#from companies.models import Company, Executives, Directors


#class DirectorInline(admin.TabularInline):
    #model = Directors
#class ExecutivesInline(admin.TabularInline):
    #model = Executives

class PersonAdmin(admin.ModelAdmin):
    search_fields=["first_name", "last_name",]
    filter_horizontal = ['nationality']
    #filter_horizontal = ( 'documents', )
    #filter_vertical = ('documents', 'web_references')
    #inlines = [DirectorInline, ExecutivesInline]
    
admin.site.register(Person, PersonAdmin)
