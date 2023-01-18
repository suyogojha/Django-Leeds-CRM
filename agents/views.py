from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixins
from django.core.mail import send_mail
import random
class AgentListView(OrganisorAndLoginRequiredMixins, generic.ListView):
    template_name = "agents/agent_list.html"
    
    # here we have filtered the user created agent this will only show the agents created by specific  users that we are logged in 
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)



class AgentCreateView(OrganisorAndLoginRequiredMixins, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organization = self.request.user.userprofile
        )
        send_mail(
            subject = "You are invited to be an agent",
            message="You're added as an agent.Please login to procide further. ",
            from_email= "admin@admin.com",
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    
    
class AgentDetailView(OrganisorAndLoginRequiredMixins, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)    
    
class AgentUpdateView(OrganisorAndLoginRequiredMixins, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")

    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
    
        
class AgentDeleteView(OrganisorAndLoginRequiredMixins, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)

    def get_success_url(self):
        return reverse("agents:agent-list")