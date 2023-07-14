from django.contrib import admin

from .models import Blockchain,Block
# Register your models here.
admin.site.register([Blockchain])
admin.site.register([Block])
