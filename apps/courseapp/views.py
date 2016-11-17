from django.shortcuts import render, redirect, HttpResponse
from . models import Course

# Create your views here.

def index(request):
	courses = Course.objects.all()
	context = { 'courses':courses,
    }
	return render(request, 'courseapp/index.html',context)

def create(request):
		Course.objects.create(name=request.POST['name'], description=request.POST['description'])
		return redirect('/')



def destroy(request, id):
	context = {
	'remove': Course.objects.get(id=id),
	}
	return render(request, 'courseapp/destroy.html', context)

def remove(request, id):
	delete =  Course.objects.get(id=id)
	if request.POST['button'] == 'Yes! I want to delete this':
		delete.delete()
	elif request.POST['button'] == 'No':
		pass 
	return redirect('/')

