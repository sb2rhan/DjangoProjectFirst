from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# every controller must have 1 argument and return HttpResponse
def index(request):
    # return HttpResponse('<h1>Post page</h1>')
    # let's use shortcuts module
    return render(request, 'post/index.html') # from templates directory

def detail(request, id):
    # return HttpResponse(f'<h1>Blog post #{id}</h1>')
    return render(request, 'post/details.html')
