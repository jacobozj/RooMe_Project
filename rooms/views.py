from django.shortcuts import render, get_object_or_404
from .models import Rooms

# Create your views here.
def index(request):
    rooms=Rooms.objects.all()
    return render(request, 'pages/index.html', {'rooms': rooms})

def room(request, id):
    rooms = get_object_or_404(Rooms, pk=id)

    context = {
        'rooms': rooms
    }

    return render(request, 'rooms/rooms.html', context)