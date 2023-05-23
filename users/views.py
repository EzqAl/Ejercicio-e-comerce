from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomAuthenticationForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from .forms import CheckoutForm


def login_view(request):
    if not request.user.is_authenticated:  # ToDo: averiguar el decorador is_authenticated
        if request.method == 'POST':
            form = CustomAuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('ecommerce:home')
            else:
                messages.error(request, form.errors)
                #messages.error(request, "Usuario y/o contraseña inválido/a")
                return render(request, 'users/login.html', {'form': form})        
        else:
            return render(request, 'users/login.html', {'form': CustomAuthenticationForm})
    else:
        messages.error(request, 'Ya estás logueado en el sitio')
        return redirect('ecommerce:home')
    

def logout_view(request):
    logout(request)
    return redirect('ecommerce:home')


def signup_view(request):
    if not request.user.is_authenticated:  # ToDo: averiguar el decorador is_authenticated
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, '¡Tu cuenta ha sido creada correctamente! Ya podés iniciar sesión.')
                return redirect('users:login')
            else:
                messages.error(request, form.errors)
                return render(request, 'users/signup.html', {'form': form})
        else:
            return render(request, 'users/signup.html', {'form': CustomUserCreationForm})
    else:
        messages.error(request, 'Ya estás logueado en el sitio')
        return redirect('ecommerce:home')
    

def checkout_confirmacion(request):
    
    return render(request, 'checkout/confirmacion.html')
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario y finaliza la compra
            # según tus requerimientos

            # Ejemplo: Guardar los datos del formulario en la base de datos
            form.save()

            # Redireccionar a la página de confirmación de compra
            return redirect(reverse('checkout_confirmacion'))
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form})