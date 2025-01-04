from django.shortcuts import redirect, render
from .models import Pet, Blog
from .forms import AddPetForm, BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "pet_app/home.html")

def pets(request):
    pets = Pet.objects.all()
    return render(request, "pet_app/pets.html", {"pets": pets})
@login_required
def add_pet_form(request):
    if request.method == 'POST':
        form = AddPetForm(request.POST)
        if form.is_valid():
            pet_data = form.cleaned_data
            print(pet_data)
            new_pet =Pet(
                petName=pet_data['petName'],
                petAge= pet_data['petAge'],
                petBread=pet_data['petBread'],
                petImage=pet_data['petImage'],
            )
            new_pet.save()
            return redirect('pets')
            
    else:

        form = AddPetForm()
    return render(request, "pet_app/add_pet.html", {'form': form})

@login_required
def create_blog(request):
    blog_form = BlogForm(request.POST)
    if request.method == "POST":
        if blog_form.is_valid():
            
            blog_data = blog_form.cleaned_data
            print(blog_data)
            new_blog = Blog(
                title = blog_data['title'],
                content = blog_data['content']
            )
            new_blog.save()
            return redirect('get_blog')
        
    else:
        blog_form
    return render(request, "pet_app/create_blog.html",{'blog_form': blog_form})


def blog(request):
    blog = Blog.objects.all()
    return render(request, "pet_app/blogs.html", {'blogs': blog})