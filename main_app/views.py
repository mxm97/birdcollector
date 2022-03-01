from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird, Toy
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()

    # print(bird.toys.all().values_list('id'))

    toys_bird_doesnt_have = Toy.objects.exclude(id__in = bird.toys.all().values_list('id'))

    return render(request, 'birds/detail.html', { 
        'bird': bird,
        'feeding_form': feeding_form,
        'toys': toys_bird_doesnt_have,
    })

def add_feeding(request, bird_id):
    # 1) collect form input values
    form = FeedingForm(request.POST)
    # 2) valid input values
    if form.is_valid():
        # 3) save a copy of a new feeding instance in memory
        new_feeding = form.save(commit=False)
        # 4) attach a reference to the cat that owns the feeding
        new_feeding.bird_id = bird_id
        # 5) save the new feeding to the database
        new_feeding.save()
    # 6) redirect the user back to the detail
    return redirect('detail', bird_id=bird_id)

# Renders a template with a form on it
# Creates a model form based on the model
# Responds to GET and POST requests
#  1) GET render the new bird form
#  2) POST submit the form to create a new instance
# Validate form inputs
# Handles the necessary redirect following a model instance creating

def assoc_toy(request, bird_id, toy_id):
    Bird.objects.get(id=bird_id).toys.add(toy_id) # gets the bird from the db and adds a toy to the cat based on it's id
    return redirect('detail', bird_id)

# Class Based Views
class BirdCreate(CreateView):
    model = Bird
    fields = '__all__'

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class BirdDelete(DeleteView):
    model = Bird
    success_url = '/birds/'

class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')


class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'


class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'