from django.urls import path
from blog import views

urlpatterns = [
	path('',views.blog, name='blog'),
	path('<slug:slug>/',views.blog_details, name='blog-details'),
]