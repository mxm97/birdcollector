from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', { 'bird': bird })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        # 3) save a copy of a new feeding instance in memory
        new_feeding = form.save(commit=False)
        # 4) attach a reference to the cat that owns the feeding
        new_feeding.bird_id = bird_id
        # 5) save the new feeding to the database
        new_feeding.save()
    # 6) redirect the user back to the detail
    return redirect('detail', bird_id=bird_id)

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