from django.shortcuts import render
from recipe.models import Recipe
from recipe.forms import RatingForm
from django.views.generic.edit import CreateView


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    title   = "Home"
    context = { 'recipes':recipes, 'title':title }
    return render(request, 'recipe/index.html', context)

def create(request):
    form = RecipeForm()
    return render(request, 'recipe/create.html', { 'form':form })

class RecipeStore(CreateView):
    success_url = '/'
    model = Recipe
    fields = ['title', 'prep_time', 'cooking_time', 'serves','ingredients', 'cooking_instructions', 'image']

def show(request, id):
    form = RatingForm()
    recipe = Recipe.objects.get(id = id)
    return render(request, 'recipe/show.html', {'recipe':recipe, 'form':form})
