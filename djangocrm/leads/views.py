from leads.models import Lead, Agent
from django.shortcuts import render, redirect
from django.http import HttpResponse
from leads.form import LeadForm, LeadModelForm

# Create your views here.


def lead_list(request):

    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


def lead_create(request):
    form = LeadModelForm()  # Create an empty form

    # check if it'is a POST method
    if request.method == 'POST':
        print('Receiving a POST Request')
        # validating and repopulate the Form
        form = LeadModelForm(request.POST)
        # validate the form
        if form.is_valid():
            form.save()
            # Controlli non necessari se si usa un Model Form,
            # basta il metodo form.save()
            """  print(form.cleaned_data)  # Print Cleaned Data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = form.cleaned_data['agent']
            # Create the Lead into DB
            Lead.objects.create(first_name=first_name,
                                last_name=last_name, age=age,
                                agent=agent) """
            # redirect to Lead List
            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)  # Pre populate the Form

    # check if it'is a POST method
    if request.method == 'POST':
        # if we are POSTING, the instance parameter will
        # make the form.save updating and not creating
        # the instance in the DB
        form = LeadModelForm(request.POST, instance=lead)
        # validate the form
        if form.is_valid():
            form.save()
            # redirect to Lead List
            return redirect('/leads')

    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)


""" def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm()
    # check if it'is a POST method
    if request.method == 'POST':
        # validating and repopulate the Form
        form = LeadForm(request.POST)
        # validate the form
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            # Save data in the form in the lead
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.agent = agent

            # Update the DB value
            lead.save()

            # redirect to Lead List
            return redirect('/leads')

    context = {
        "lead": lead,
        "form": form
    }
    return render(request, "leads/lead_update.html", context) """
