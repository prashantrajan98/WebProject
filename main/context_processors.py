from .forms import SubscriptionForm
from service.models import Services

def subscription(request):
	sf = SubscriptionForm()

	return {
		'sf' : sf,
		'service': Services.objects.all()
	}
