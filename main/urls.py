from django.urls import path
from main import views

urlpatterns = [
	path('',views.index, name='index'),
	path('contact/',views.contact, name='contact'),
	path('about/',views.about, name='about'),
	path('status/',views.status, name='status'),
	path('subscribe/',views.subscription, name='subscribe'),
]