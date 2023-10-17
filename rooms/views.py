from django.shortcuts import render, get_object_or_404
from .models import Rooms
from django.db.models import Q

# Create your views here.
def index(request):
    bedroom_choices = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10}
    
    price_choices = {'1000000': '$1,000,000', '2000000': '$2,000,000', '3000000': '$3,000,000',
                     '4000000': '$4,000,000', '5000000': '$5,000,000', '6000000': '$6,000,000', 
                     '7000000': '$7,000,000', '8000000': '$8,000,000', '9000000': '$9,000,000',
                     '10000000': '$10,000,000+',}
    
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