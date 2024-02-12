from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Farm
from .forms import FarmForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def farm_dashboard(request):
    template_name = 'farm/farm_dashboard.html'
    return render(request, template_name)


def farm_create_update(request, farm_id=None):
    template_name = 'farm/farm_create_update.html'
    if farm_id:
        farm = get_object_or_404(Farm, id=farm_id)
    else:
        farm = None
    
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            farm = form.save()
            return redirect('farm:farm_detail', farm_id=farm.id)
    else:
        form = FarmForm(instance=farm)

    return render(request, template_name, {'form': form})

def farm_list(request):
    template_name = 'farm/farm_list.html'
    farms = Farm.objects.all()
    paginator = Paginator(farms, 1)  # Show 1 farms per page

    page_number = request.GET.get('page')
    try:
        farms = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        farms = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        farms = paginator.page(paginator.num_pages)
    return render(request, template_name, {'farms': farms})

def farm_detail(request, farm_id):
    template_name = 'farm/farm_detail.html'
    farm = get_object_or_404(Farm, id=farm_id)
    # Find the next farm
    next_farm = Farm.objects.filter(location=farm.location,pk__gt=farm.pk).first()
    # Find the previous farm
    previous_farm = Farm.objects.filter(location=farm.location,pk__lt=farm.pk).last()
    context = {'farm': farm,
               'next_farm': next_farm,
                'previous_farm': previous_farm,}
    return render(request, template_name, context)
