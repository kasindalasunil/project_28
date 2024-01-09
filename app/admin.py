from django.contrib import admin

# Register your models here.

from app.models import *


class customizewebpage(admin.ModelAdmin):
    #it is going to display every column 
    list_display=['topic_name','name','url','email']
    #it is going to make everything hyperlink
    list_display_links=['name','url']
    #it will make editable
    list_editable=['email']
    list_filter=['name']
    search_fields=['name']
    list_per_page=2



admin.site.register(Topic)

admin.site.register(Webpage,customizewebpage)

admin.site.register(AccessRecord)



