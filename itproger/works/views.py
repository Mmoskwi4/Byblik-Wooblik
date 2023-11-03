from django.shortcuts import render
from .models import Completed

# Create your views here.
def works(request):
    comleted = Completed.objects.all()
    context = {
        'completed': comleted
    }
    return render(request, 'works/works.html', context)