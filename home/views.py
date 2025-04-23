from django.shortcuts import render
from products.models import Customer
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.POST.get('username')
        password1 = data.POST.get('password1')
        password2 = data.POST.get('password2')
        email = data.POST.get('email')
        
        if not username or not password1 or not password2:
            messages.error(request, "Faltan datos")
        
        elif _validate_pass(password1, password2):
            messages.error(request, "Las contraseñas no coinciden")
        
        elif Customer.objects.filter(username=username).exists():
            messages.error(request, "El usuario esta en uso")


        else:
            Customer.objects.create(
                username=username,
                password=password1,
                email=email,
            )
        
        

    """ aca el method es GET """
    return render(
        request,
        'accounts/register.html',
        )

""" esta logica va en un repo aparte """
def _validate_pass(password1, password2):
    print(password1 == password2)
    password1 == password2