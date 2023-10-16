from django.shortcuts import render, get_object_or_404
from .models import Rooms
from django.db.models import Q

# Create your views here.
def index(request):
    busqueda=request.GET.get("city")
    print(busqueda)
    rooms=Rooms.objects.all()

    if busqueda:
        rooms=Rooms.objects.filter(
            Q(location__icontains=busqueda)
        ).distinct()


    return render(request, 'pages/index.html', {'rooms': rooms})

def room(request, id):
    rooms = get_object_or_404(Rooms, pk=id)
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms/rooms.html', context)