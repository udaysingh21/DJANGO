from django.contrib import admin
from firstapp.models import Topic,AccessRecord,Webpage
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)


