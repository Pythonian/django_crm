from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LeadForm, RegisterForm
from .models import Agent, Lead


def home(request):
    """
    Returns the Home page.

    Template: ``home.html``
    """
    
    template_name = 'home.html'
    context = {}

    return render(request, template_name, context)


@login_required
def lead_list(request):
    """
    Returns the page for viewing all leads.

    Template: ``leads/lead_list.html``
    Context:
        leads
            A list of active Lead objects
    """
    leads = Lead.objects.filter(is_active=True)
    
    template_name = 'leads/lead_list.html'
    context = {
        "leads": leads,
    }

    return render(request, template_name, context)


@login_required
def lead_detail(request, pk):
    """
    Returns the detail page of a Lead.

    Template: ``leads/lead_detail.html``
    Context:
        lead
            A Lead object instance
    """
    lead = get_object_or_404(Lead, pk=pk, is_active=True)
    
    template_name = 'leads/lead_detail.html'
    context = {
        "lead": lead,
    }

    return render(request, template_name, context)


@login_required
def lead_create(request):
    """
    Returns the form page for creating a Lead.

    Template: ``leads/lead_form.html``
    Context:
        form
            LeadForm object
    """
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES)
        if form.is_valid():
            new_lead = form.save()
            send_mail(
                subject="A lead has been created",
                message="Go to the site to view the new lead",
                from_email="test@example.com",
                recipient_list=["receiver@example.com"]
            )
            return redirect(new_lead.get_absolute_url())
    else:
        form = LeadForm()

    template_name= 'leads/lead_create.html'
    context = {
        'form': form,
    }

    return render(request, template_name, context)


@login_required
def lead_update(request, pk):
    """
    Returns the form page for updating a Lead.

    Template: ``leads/lead_form.html``
    Context:
        form
            LeadForm object
        lead
            Lead object 
    """
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, request.FILES, instance=lead)
        if form.is_valid():
            form.save()
            # return redirect(new_lead.get_absolute_url())
            return redirect('/')
    else:
        form = LeadForm(instance=lead)

    template_name= 'leads/lead_update.html'
    context = {
        'form': form,
        'lead': lead,
    }

    return render(request, template_name, context)


@login_required
def lead_delete(request, pk):
    """
    Returns a lead delete confirmation page.

    Templates: ``leads/lead_delete_confirm.html``
    Context:
        lead
            Lead object
    """
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.is_active = False
        lead.save()
        return redirect('/')

    template_name= 'leads/lead_delete_confirm.html'
    context = {
        'lead': lead,
    }

    return render(request, template_name, context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('login')
    else:
        form = RegisterForm()

    template_name= 'registration/signup.html'
    context = {
        'form': form,
    }

    return render(request, template_name, context)
