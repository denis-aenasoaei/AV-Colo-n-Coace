from django.shortcuts import render


def index(request):
    """HOME PAGE"""
    return render(request, 'index.html')


def map(request):
    """MAP PAGE"""
    return render(request, 'map.html')