from django.shortcuts import render

# Create your views here.

def stored_xss_view(request):
    return render(request, 'stored_xss/stored_xss.html',{})

def introduction_view(request):
    return render(request, 'stored_xss/introduction.html', {})

def level1_view(request):
    return render(request, 'stored_xss/level1.html', {})

def level2_view(request):
    return render(request, 'stored_xss/level2.html', {})
