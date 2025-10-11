from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import House, Applicant
from .forms import ApplicantForm
from django.db import models


def house_list(request):
    """Display available houses with search and price filtering."""
    houses = House.objects.filter(availability=True)

    # Get filters from GET parameters
    location_query = request.GET.get('location', '').strip()
    max_rent = request.GET.get('max_rent')

    # Apply location search (case-insensitive partial match)
    if location_query:
        houses = houses.filter(
            models.Q(title__icontains=location_query) |
            models.Q(address__icontains=location_query)
        )

    # Apply max rent filter
    if max_rent and max_rent.isdigit():
        houses = houses.filter(rent__lte=float(max_rent))

    return render(request, 'housing/house_list.html', {
        'houses': houses,
        'location_query': location_query,
        'max_rent': max_rent,
    })


def house_detail(request, pk):
    """Show details of a specific house."""
    house = get_object_or_404(House, pk=pk)
    return render(request, 'housing/house_detail.html', {'house': house})


@login_required
def apply_for_house(request, pk):
    """Allow logged-in users to apply for a house."""
    house = get_object_or_404(House, pk=pk)
    
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicant = form.save(commit=False)
            applicant.applied_house = house
            applicant.user = request.user
            applicant.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('housing:application_status', applicant_id=applicant.id)
    else:
        # Pre-fill name from user profile if available
        initial_name = request.user.get_full_name() or request.user.username
        form = ApplicantForm(initial={'name': initial_name})
    
    return render(request, 'housing/application_form.html', {
        'form': form,
        'house': house
    })


@login_required
def application_status(request, applicant_id):
    """Show application status for the logged-in user."""
    applicant = get_object_or_404(Applicant, id=applicant_id, user=request.user)
    return render(request, 'housing/application_status.html', {'applicant': applicant})


class SignUpView(CreateView):
    """Handle user registration."""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'