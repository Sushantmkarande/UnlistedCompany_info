from django.shortcuts import render

# Create your views here.
from .models import Data
import json



def index(request):
    data = Data.objects.all()
    context = {'data': data}
    return render(request, 'Api/index.html', context)
