from django.shortcuts import render, redirect
from service.models import Services
from blog.models import Blog
from .forms import ContactForm, TrackForm, SubscriptionForm
from .models import About, Track, TrackStatus, Subscription, HomePageSeo, AboutPageSeo
# Create your views here.
def index(request):
	service = Services.objects.all()
	blog_posts = Blog.objects.order_by('-id')[0:3]
	seo = HomePageSeo.objects.all()
	context = {
	'service' : service,
	'blog_posts': blog_posts,
	'seo': seo
	}
	return render(request, 'index.html', context)

def contact(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():	
			form.save()
			return redirect('index')
	context = {
		'form': form
	}
	return render(request,'contact.html',context)

def about(request):
	about_us = About.objects.all()
	seo = HomePageSeo.objects.all()
	context = {
		'about_us':about_us,
		'seo': seo
	}
	return render(request, 'about.html', context)

def status(request):
	bill = request.GET.get('bill')
	tracks = Track.objects.filter(bill=bill)
	trcak_status = TrackStatus.objects.all()

	context = {
		'bill': bill,
		'tracks': tracks,
		'trcak_status' : trcak_status
	}
	return render(request, 'status.html',context)

def subscription(request):
	if request.method == 'POST':
		sf = SubscriptionForm(request.POST)
		if sf.is_valid():
			sf.save()
			return redirect('index')