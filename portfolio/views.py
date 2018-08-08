from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    items = models.Portfolio.objects.all()
    return render(request, "portfolio/index.html", {"items": items})