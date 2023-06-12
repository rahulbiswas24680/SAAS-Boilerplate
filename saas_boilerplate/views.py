from django.shortcuts import render

def home(request):
    return render(request, 'home.html', context={})

def pricing(request):
    return render(request, 'pricing.html', context={})

def blog(request):
    return render(request, 'blog.html', context={})

def team(request):
    return render(request, 'team.html', context={})