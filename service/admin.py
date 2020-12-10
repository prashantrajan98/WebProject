from django.contrib import admin
from .models import Services

# Register your models here.
class ServicesInline(admin.TabularInline):
	model = Services

class ServicesAdmin(admin.ModelAdmin):
	inline = [ServicesInline,]

admin.site.register(Services, ServicesAdmin)

