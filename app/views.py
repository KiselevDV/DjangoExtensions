from django.http import HttpResponse


def hello_world(request):
    """Print text 'Hello World!'"""
    return HttpResponse("Hello World!")
