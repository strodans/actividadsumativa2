# views.py
from django.shortcuts import render,redirect
from .models import Usuario, Inventario, Categoria

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        print("Datos del form", username,password)
        #return render(request, 'core/login_usuario.html')
        usuarioBD = Usuario.objects.filter(username=username).first()
        print(usuarioBD)
        if usuarioBD is not None:
           if usuarioBD.password == password:
              if usuarioBD.perfil == 1:
                 print("Home administrador")
                 return redirect('home')
              if usuarioBD.perfil == 2:
                 print("Home usuario")
                 return redirect('home')
              else:
                 print("No se encontró perfil")
                 return render(request,'core/login_usuario.html')
           else: 
              print("Passwrod Incorrecto")
              return render(request,'core/login_usuario.html')
        else:
           print("Usuario no existe")
           return render(request,'core/login_usuario.html')
    else:
     return render(request,'core/login_usuario.html')
    
def home(request):
    inventarios = Inventario.objects.all()
    datos = {
       'inventario' : inventarios
    }
    print(datos)
    return render(request,'core/home.html',datos)
