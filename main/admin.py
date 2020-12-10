from django.contrib import admin
from .models import Contact, About, Track, TrackStatus, Subscription, HomePageSeo, AboutPageSeo

# Register your models here.
class TrackStatusInline(admin.TabularInline):
	model = TrackStatus

class TrackAdmin(admin.ModelAdmin):
	inlines = [TrackStatusInline,]


admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Track, TrackAdmin)
admin.site.register(Subscription)
admin.site.register(HomePageSeo)
admin.site.register(AboutPageSeo)