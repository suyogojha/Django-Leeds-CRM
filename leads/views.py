from django.shortcuts import render, redirect
from .models import Lead, Agent
from django.http import HttpResponse
from .forms import *

# import for class based view 
from django.views.generic import TemplateView

# same thing as class based view shown as above 
# class LandingpageView(TemplateView):
#     template_name = "landing.html" 




# function based view 
def landing_page(request):
    return render(request, "landing.html")
    



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)


def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)


# lead create start

def lead_create(request):
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
    

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
       form = LeadModelForm(request.POST, instance=lead)
       if form.is_valid():
           form.save()
           return redirect("/leads")
    context = {
        "form": form,
        "lead": lead,
    }
    return render(request, "leads/lead_update.html", context)
    
    


#lead update end


#lead delete start

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")
    







