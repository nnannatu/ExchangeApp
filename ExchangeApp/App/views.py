from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'index.html'
    return render(request, template)

def about(request):
    template = 'about.html'
    return render(request, template)