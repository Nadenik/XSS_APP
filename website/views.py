from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # Get all Posts

    # Render app template with context
    return render(request, 'website/index.html',{})