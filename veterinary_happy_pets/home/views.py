from django.shortcuts import render

# Vista de la página de principal
def index(request):
    return render(request, 'home/index.html')
