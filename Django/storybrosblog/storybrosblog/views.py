from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Home Page')

def about(request):
    return HttpResponse('About')
