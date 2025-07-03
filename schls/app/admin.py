from django.contrib import admin

# Register your models here.
from .models import coursedetails,Applymodel
admin.site.register(coursedetails)
admin.site.register(Applymodel)