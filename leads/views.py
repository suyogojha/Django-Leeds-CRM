from django.shortcuts import render, redirect, reverse
from .models import Lead, Agent
from django.views import generic
from django.http import HttpResponse
from .forms import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# sending mail
from django.core.mail import send_mail
from agents.mixins import OrganisorAndLoginRequiredMixins

# import for class based view 
from django.views.generic import TemplateView

# same thing as class based view shown as above 
# class LandingpageView(TemplateView):
#     template_name = "landing.html" 

# for signup

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")


# function based view 
def landing_page(request):
    return render(request, "landing.html")
    

# class based create lead 
class LeadCreateView(OrganisorAndLoginRequiredMixins, generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")

    # sending email 
    def form_valid(self, form):
        send_mail(
            subject = "A lead has been created",
            message = "Go to the site to see new leads",
            from_email = "test@test.com",
            recipient_list = ["test2@test.com"] 
        )
        return super(LeadCreateView, self).form_valid(form)
            
# @login_required       
# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "leads": leads
#     }
#     return render(request, "leads/lead_list.html", context)


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    
    def get_queryset(self):
        user = self.request.user
        
        # initial queryset of leads for the entire organization 
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.userprofile, agent__isnull=False)
            
            # filter for the agent that is logged in 
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=True
            )
            context.update({
                "unassigned_leads": queryset
            })
        return context
            



@login_required
def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


# lead create start
@login_required
def lead_create(request, OrganisorAndLoginRequiredMixins):
    form = LeadModelForm()
    if request.method == "POST":
        print("Receving a POST request")
        form = LeadModelForm(request.POST)
        if form.is_valid():
        #     print("the form is valid")
        #     print(form.cleaned_data)
        #     first_name = form.cleaned_data['first_name']
        #     last_name = form.cleaned_data['last_name']
        #     age = form.cleaned_data['age']
        #     agent = form.cleaned_data['agent']
        #     Lead.objects.create(
        #         first_name = first_name,
        #         last_name = last_name,
        #         age = age,
        #         agent = agent
        #     )
        #we can use the details as shown up or we can just add save function to save the data in model form 
            form.save()
            print("The Lead has been created")
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "leads/lead_create.html", context)
    
    
    
    
    # we can also use this to create the form  
# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         print("Receving a POST request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print("the form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print("The Lead has been created")
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
    
    
# lead create end here



#lead update start

# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         print("Receving a POST request")
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print("the form is valid")
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead,
#     }
#     return render(request, "leads/lead_update.html", context)
    
    
    
# @login_required
# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#        form = LeadModelForm(request.POST, instance=lead)
#        if form.is_valid():
#            form.save()
#            return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead,
#     }
#     return render(request, "leads/lead_update.html", context)
    
    
class LeadUpdateView(OrganisorAndLoginRequiredMixins, generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization 
        return Lead.objects.filter(organisation=user.userprofile)


#lead update end


#lead delete start
# @login_required
# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
    

class LeadDeleteView(OrganisorAndLoginRequiredMixins, generic.UpdateView):
    
    def get_success_url(self):
        return reverse("leads:lead-list")    
    
    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organization 
        return Lead.objects.filter(organisation=user.userprofile)





class AssignAgentView(OrganisorAndLoginRequiredMixins, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm
    
    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
    
    def get_success_url(self):
        return reverse("leads:lead-list")    
    
    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)
    
    
    
    
    
    
    
    
    