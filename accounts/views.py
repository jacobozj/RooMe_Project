from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Users
from rooms.models import Reserva


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
        user = Users.objects.get(username=request.user)
        room = Reserva.objects.filter(usuario_id=user.id)
        return render(request, 'accounts/dashboard.html', {'room': room})
    else:
        return redirect('login')
