from django.shortcuts import render
from .models import Pet
# Create your views here.


def home(request):
    return render(request, "pet_app/home.html")

def pets(request):
    pets = Pet.objects.all()
    return render(request, "pet_app/pets.html", {"pets": pets})