from django.shortcuts import render, redirect
from .models import Lead, Agent
from django.http import HttpResponse
from .forms import *

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
    
    
    
    










