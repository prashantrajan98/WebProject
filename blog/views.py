from django.shortcuts import render
from .models import Blog, BlogPageSeo


# Create your views here.
def blog(request):
	blogs = Blog.objects.all()
	latest_posts = Blog.objects.order_by('-id')[0:2]
	seo = BlogPageSeo.objects.all()
	context = {
		'blogs':blogs,
		'latest_posts':latest_posts,
		'seo': seo
	}
	return render(request, 'blog/blog.html', context)


def blog_details(request, slug):
	blog = Blog.objects.get(slug=slug)
	latest_posts = Blog.objects.all()[0:2]

	context = {
		'blog': blog,
		'latest_posts': latest_posts
	}
	return render(request, 'blog/blog-details.html', context)