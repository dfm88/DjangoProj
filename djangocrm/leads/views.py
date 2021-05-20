from leads.models import Lead, Agent
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from leads.form import LeadForm, LeadModelForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.forms import UserCreationForm

# CLASS Based Sign UP


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):  # special method
        # reverse = special key of django.shortcut to read the namespace from URL
        return reverse("login")


# CLASS Based Template
class LandingPageView(TemplateView):
    template_name = "landing.html"

# FUNCTION Based Template


def landing_page(request):
    return render(request, "landing.html")

# CLASS Based List
# NO context passed, it automaticallt takes it fomr model under "object_list" key
# Or ita can be customized with "context_object_name" attribute


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


# FUNCTION Based List
def lead_list(request):

    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


# CLASS Based Detail
class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

# FUNCTION Based Detail


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


# CLASS Based Create
class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):  # special method
        # reverse = special key of django.shortcut to read the namespace from URL
        return reverse("leads:lead-list")

    def form_valid(self, form):  # special method
        nome = form.cleaned_data['first_name']
        send_mail("User Created", f'the user {nome} was created', [
                  'test@test.com'], ['testRec@test.com'])

        return super(LeadCreateView, self).form_valid(form)


# FUNCTION Based Create


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
            return redirect('/leads')

    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

# CLASS Based Update


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):  # special method
        # reverse = special key of django.shortcut to read the namespace from URL
        return reverse("leads:lead-list")

# FUNCTION Based Update


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


# CLASS Based Delete

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# FUNCTION Based Delete


def lead_delete(request, pk):
    Lead.objects.get(id=pk).delete()
    return redirect('/leads')


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
