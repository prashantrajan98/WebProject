from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=150)
	slug = models.CharField(max_length=120, unique=True)
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_desc = models.TextField(null=True, blank=True)
	seo_keywords = models.TextField(null=True, blank= True)
	thumbnail = models.ImageField(upload_to="blog/images/")
	content = RichTextField(blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-details', kwargs={
			"slug":self.slug
			})

class BlogPageSeo(models.Model):
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_desc = models.TextField(null=True, blank=True)
	seo_keywords = models.TextField(null=True, blank= True)

	def __str__(self):
		return self.seo_title