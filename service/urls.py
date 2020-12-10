from django.urls import path
from service import views

urlpatterns = [
	path('<slug:slug>/',views.service, name='service'),
]