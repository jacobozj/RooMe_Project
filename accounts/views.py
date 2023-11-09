from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Users, Reseña
from rooms.models import Reserva, Rooms
import matplotlib.pyplot as plt
from collections import Counter

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                messages.success(request, 'Has iniciado sesion como admin.')
                return redirect('/admin/')
            else:
                auth.login(request, user)
                messages.success(request, 'Has iniciado sesion como usuario.')
                return redirect('dashboard')
        else:
            messages.error(request, 'Los datos son incorrectos')
            return redirect('login')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        carrera = request.POST['carrera']
        genero = request.POST['genero']
        tipo=request.POST['perfil']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Usuario ya esxiste!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email ya existe!')
                    return redirect('register')
                else:
                    if tipo=="estudiante":
                        user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                        usuario=Users(user.id, firstname, lastname, username, email, password, confirm_password, carrera,genero,tipo)
                        usuario.save()

                        auth.login(request, user)
                        messages.success(request, 'Has iniciado sesion como usuario.')
                        return redirect('dashboard')
                    elif tipo=="admin":
                        user = User.objects.create_superuser(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                        usuario=Users(user.id, firstname, lastname, username, email, password, confirm_password, carrera,genero,tipo)
                        usuario.save()

                        auth.login(request, user)
                        messages.success(request, 'Has iniciado sesion como admin.')
                        return redirect('/admin/')
                    
                    #user.save()
                    #messages.success(request, 'Te has registrado exitosamente.')
                    #return redirect('login')
        else:
            messages.error(request, 'Contraseña no coincide')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        if Reserva.objects.filter(usuario_id=request.user.id):
            reserva = Reserva.objects.get(usuario_id=request.user.id)
            room = Rooms.objects.get(id=reserva.habitacion_id)
            return render(request, 'accounts/dashboard.html', {'room': room, 'reserva': reserva})
        else:
            return render(request, 'accounts/dashboard.html')
    else:
        return redirect('login')
    
def graficar(campo):
    valores=Users.objects.values_list(campo, flat=True)
    conteo=dict(Counter(valores))
    plt.bar(conteo.keys(), conteo.values())
    plt.xlabel(campo)
    plt.ylabel('Cantidad')
    plt.title(f'Gráfico de {campo}')
    plt.xticks(rotation=90)
    plt.yticks(range(min(conteo.values()), max(conteo.values()) + 1))
    plt.show()


def datos(request):
    campos=['sex', 'program']
    for campo in campos:
        graficar(campo)
    return redirect('index')


def reseña(request):
    if request.user.is_authenticated:
        users=Users.objects.get(username=request.user)
        reseña=request.POST.get("reseña")
        Reseña.objects.create(usuario=users, reseña=reseña)
        messages.success(request, 'Reseña enviada.')
        return redirect('index')

    else:
        messages.error(request, "Inicie sesión para comentar.")
        return redirect('login')