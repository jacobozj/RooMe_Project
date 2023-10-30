from django.shortcuts import render, get_object_or_404, redirect
from .models import Rooms, Reserva
from accounts.models import Users
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def index(request):
    bedroom_choices = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
    
    price_choices = {'400000': '$400,000', '800000': '$800,000', '1200000': '$1,200,000',
                     '1600000': '$1,600,000', '2000000': '$2,000,000', '2400000': '$2,400,000',
                     '2800000': '$2,800,000', '3200000': '$3,200,000', '3600000': '$3,600,000',
                     '4000000': '$4,000,000'}
    
    state_choices = {'AMA': 'Amazonas', 'ANT': 'Antioquia', 'ARA': 'Arauca', 'ATL': 'Atlántico', 'BOL': 'Bolívar',
                     'BOY': 'Boyacá', 'CAL': 'Caldas', 'CAQ': 'Caquetá', 'CAS': 'Casanare', 'CAU': 'Cauca', 'CES': 'Cesar',
                     'CHO': 'Chocó', 'COR': 'Córdoba', 'CUN': 'Cundinamarca', 'GUA': 'Guainía', 'GUV': 'Guaviare',
                     'HUI': 'Huila', 'GUV': 'La Guajira', 'MAG': 'Magdalena', 'MET': 'Meta', 'NAR': 'Nariño', 
                     'NDS': 'Norte de Santander', 'PUT': 'Putumayo', 'QUI': 'Quindío', 'RIS': 'Risaralda', 'SAP': 'San Andrés y Providencia',
                     'SAN': 'Santander', 'SUC': 'Sucre', 'TOL': 'Tolima', 'VAL': 'Valle del Cauca', 'VAU': 'Vaupés',
                     'VID': 'Vichada'}
    
    keywords=request.GET.get("keywords")
    ciudad=request.GET.get("city")
    estado=request.GET.get("state")
    cuartos=request.GET.get("bedrooms")
    precio=request.GET.get("price")
    rooms=Rooms.objects.all()

    if keywords:
        rooms=Rooms.objects.filter(Q(title__icontains=keywords))
            
    if ciudad:
        rooms=Rooms.objects.filter(Q(city__icontains=ciudad))

    if estado:
        rooms=Rooms.objects.filter(Q(state__icontains=estado))

    if cuartos:
        rooms=Rooms.objects.filter(Q(bedrooms__icontains=cuartos))
    
    if precio:
        rooms=Rooms.objects.filter(Q(price__icontains=precio))

    return render(request, 'pages/index.html', {'rooms': rooms, "bedroom_choices": bedroom_choices, 
                                                "price_choices": price_choices, "state_choices": state_choices})

def room(request, id):
    rooms = get_object_or_404(Rooms, pk=id)
    context = {
        'rooms': rooms
    }
    return render(request, 'rooms/rooms.html', context)


def about(request):
    return render(request, 'pages/about.html')

def booking(request, id):
    if request.user.is_authenticated:
        users=Users.objects.get(username=request.user)
        if users.profile=="estudiante":
            room=get_object_or_404(Rooms,pk=id)
            if room.bedrooms==room.available_bedrooms:
                messages.error(request, "Habitaciones ya reservadas.")
                room.reserved=True
                room.save()
                return redirect('index')
            else:
                Reserva.objects.create(habitacion=room, usuario=users)
                room.available_bedrooms=room.available_bedrooms+1
                room.save()
                return render(request, 'accounts/dashboard.html', {'room': room})
        else:
            messages.error(request, "No puede reservar como admin.")
            return redirect('login')
    else:
        messages.error(request, "Inicie sesión para reservar.")
        return redirect('login')