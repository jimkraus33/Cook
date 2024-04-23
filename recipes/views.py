from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import UpdateRecipeForm, CreateRecipeForm
from django.contrib import messages



# Create your views here.
@login_required(login_url='login')
def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {
        'recipes': recipes
    })



@login_required(login_url='login')
def view(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.directions = recipe.directions.split('\n')
    recipe.ingredients = recipe.ingredients.split('\n')
    return render(request, 'recipes/view.html', {
        'recipe': recipe
    })


@login_required(login_url='login')
def update(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = UpdateRecipeForm(instance=recipe)
    if request.method == 'POST':
        form = UpdateRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated!')
            return HttpResponseRedirect(reverse_lazy('index'))
    return render(request, 'recipes/update.html', {
        'form': form
    })


@login_required(login_url='login')
def create(request):    
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe created!')
        else:
            context = {'form': form}
            return render(request, 'recipes/create.html', context)
    return render(request, 'recipes/create.html', {
        'form': CreateRecipeForm()
    })
