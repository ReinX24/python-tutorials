from django.shortcuts import render

from pizzas.models import Pizza

# Create your views here.
def index(request):
    """Home page for our pizzas app."""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Webpage for our Pizzas."""
    pizzas = Pizza.objects.all()
    context = {"pizzas": pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def toppings(request, pizza_id):
    """Webpage for topping for each pizza."""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {"pizza": pizza, "toppings": toppings}
    return render(request, 'pizzas/toppings.html', context)