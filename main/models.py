from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=120)
	email = models.EmailField()
	website = models.CharField(max_length=120)
	phone = models.IntegerField()
	message = models.TextField()

	def __str__(self):
		return self.name

class About(models.Model):
	image =  models.ImageField(upload_to='about/photos/')
	content = models.TextField()

	def __str__(self):
		return '{}'.format(self.id)

class Track(models.Model):
	bill = models.CharField(max_length=120, unique=True)
	forwarding = models.CharField(max_length=120)
	pickup = models.DateTimeField()
	destination = models.CharField(max_length=120)
	consignee = models.CharField(max_length=120)
	status = models.CharField(max_length=250, null=True)
	

	def __str__(self):
		return self.bill

class TrackStatus(models.Model):
	status = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="status_track", null=True)
	status_datetime = models.DateTimeField(null=True)
	locations= models.CharField(max_length=120, null=True)
	track_status = models.CharField(max_length=250, null=True)

	def __str__(self):
		return self.track_status

class Subscription(models.Model):
	email = models.EmailField()
	created = models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.email

class HomePageSeo(models.Model):
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_desc = models.TextField(null=True, blank=True)
	seo_keywords = models.TextField(null=True, blank= True)

	def __str__(self):
		return self.seo_title

class AboutPageSeo(models.Model):
	seo_title = models.CharField(max_length=120, null=True, blank=True)
	seo_desc = models.TextField(null=True, blank=True)
	seo_keywords = models.TextField(null=True, blank= True)

	def __str__(self):
		return self.seo_title