from django.shortcuts import render, redirect
from .models import PicGallery, UserFeedback
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext

def home(request):
	pic_list = PicGallery.objects.all().order_by('id')
	page = request.GET.get('page', 1)
	paginator = Paginator(pic_list, 12)
	try:
	    pics = paginator.page(page)
	except PageNotAnInteger:
	    pics = paginator.page(1)
	except EmptyPage:
	    pics = paginator.page(paginator.num_pages)
	return render(request, 'home.html', {'pics': pics})

def aboutus(request):
	return render(request, 'aboutus.html')

def contactus(request):
	return render(request, 'contact.html')

def post(request):
	csrfContext = RequestContext(request)
	message = request.POST['message']
	name = request.POST['name']
	subject = request.POST['subject']
	email = request.POST['email']

	form = UserFeedback()
	form.userfb = message
	form.email = email
	form.subject = subject
	form.save()
	return redirect('contactus')
