from django.contrib import admin
from . import models
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    # change the ordering of fields
    fields=['release_year','title','length']

    # search bar
    search_fields=['title','length']

    # filter
    list_filter=['release_year','length']

    # list display
    list_display=['title','release_year','length']

    # list editable - first display then edit otherwise error
    list_editable=['length']


admin.site.register(models.Movie,MovieAdmin)
admin.site.register(models.Customer)

