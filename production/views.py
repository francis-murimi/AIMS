from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from production.models import FarmingJourney
from .forms import FarmingJourneyForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def farming_journey_create_update(request, farming_journey_id=None):
    template_name = 'production/farming_journey_create_update.html'
    if farming_journey_id:
        farming_journey = get_object_or_404(FarmingJourney, id=farming_journey_id)
    else:
        farming_journey = None
    
    if request.method == 'POST':
        form = FarmingJourneyForm(request.POST, instance=farming_journey)
        if form.is_valid():
            farming_journey = form.save()
            return redirect('production:farming_journey_detail', farming_journey_id=farming_journey.id)
    else:
        form = FarmingJourneyForm(instance=farming_journey)

    return render(request, template_name, {'form': form})


def farming_journey_list(request):
    template_name = 'production/farming_journey_list.html'
    farming_journies = FarmingJourney.objects.filter(completed=False)
    paginator = Paginator(farming_journies, 1)  # Show 1 farming_journies per page

    page_number = request.GET.get('page')
    try:
        farming_journies = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        farming_journies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        farming_journies = paginator.page(paginator.num_pages)
    return render(request, template_name, {'farming_journies': farming_journies})


def farming_journey_detail(request, farming_journey_id):
    template_name = 'production/farming_journey_detail.html'
    farming_journey = get_object_or_404(FarmingJourney, id=farming_journey_id)
    # Find the next farming_journey
    next_farming_journey = FarmingJourney.objects.filter(farm__location=farming_journey.farm.location,pk__gt=farming_journey.pk).first()
    # Find the previous farming_journey
    previous_farming_journey = FarmingJourney.objects.filter(farm__location=farming_journey.farm.location,pk__lt=farming_journey.pk).last()
    context = {'farming_journey': farming_journey,
               'next_farming_journey': next_farming_journey,
                'previous_farming_journey': previous_farming_journey,}
    return render(request, template_name, context)