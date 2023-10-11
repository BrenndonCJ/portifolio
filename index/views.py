from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index/index.html')
    
def page2(request):
    return HttpResponse('Page 2')
