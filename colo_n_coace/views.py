from django.shortcuts import render


def index(request):
    """HOME PAGE"""
    return render(request, 'index.html')


def map(request, *args, **kwargs):
    """MAP PAGE"""
    search_item = -1
    if request.method == 'POST':
        search_item = request.POST["search_item"]
    else:
        if kwargs:
            search_item = kwargs["search_item"]
    return render(request, 'map.html', {'search_item': search_item})