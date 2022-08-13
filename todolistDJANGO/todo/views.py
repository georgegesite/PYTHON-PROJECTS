from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    todo =  Todo.objects.all()
    form =  TodoForm()
    context = {'todos' : todo, 'form': form}
    return render(request, 'todo\list.html', context)
 