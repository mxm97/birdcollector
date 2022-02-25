from django.shortcuts import render

# Temporary space for Bird Model
class Bird:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

birds = [
    Bird('Chip', 'Zebra Finch', 'likes to sing', 2),
    Bird('Fruit Loop', 'Toucan', 'proud of his beak', 5),
    Bird('Banana', 'Budgie', 'friendly and sociable', 1),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', { 'birds': birds })

