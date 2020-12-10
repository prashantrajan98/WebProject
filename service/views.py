from django.shortcuts import render
from .models import Services

# Create your views here.
def service(request, slug):
	our_services = Services.objects.get(slug=slug)

	context = {
		'our_services':our_services
		
	}
	return render(request, 'service/service.html', context)	