from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":        
        #save the form as new database contents
        #return to index
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary = request.POST.get('primary')
        secondary = request.POST.get('secondary')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def update(request, hero_id): 
    updated_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        updated_hero.name = request.POST.get('name')
        updated_hero.alter_ego = request.POST.get('alter_ego')
        updated_hero.primary = request.POST.get('primary')
        updated_hero.secondary = request.POST.get('secondary')
        updated_hero.catchphrase = request.POST.get('catchphrase')
        updated_hero.save()
        return HttpResponseRedirect(reverse('superheroes:update'))
    else:
        context = {
            'single_hero': updated_hero
        }
        return render(request, 'superheroes/update.html', context)

def delete(request, hero_id):
    hero = Superhero.objects.get(pk=hero_id)
    hero.delete()
    return HttpResponseRedirect(reverse('superheroes:index'))