from django.shortcuts import render

# Create your views here.
def index(request):
    productos_joyeria = [
            {
                'nombre': 'Anillo de Diamantes',
                'precio': 1250.00,
                'material': 'Oro blanco 18k'
            },
            {
                'nombre': 'Collar de Perlas',
                'precio': 599.99,
                'material': 'Plata esterlina'
            },
            {
                'nombre': 'Pulsera de Zafiros',
                'precio': 850.50,
                'material': 'Oro amarillo 14k'
            }
        ]
    contexto = {'productos': productos_joyeria}
    return render(request, 'index.html', contexto)