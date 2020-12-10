from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Services(models.Model):
	title = models.CharField(max_length=120)
	slug = models.CharField(max_length=120, unique=True, null=True)
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_desc = models.TextField(null=True, blank=True)
	seo_keywords = models.TextField(null=True, blank= True)
	image = models.ImageField(upload_to='services/photos/')
	content = RichTextField(blank=True)
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('service', kwargs={
			"slug":self.slug
			})