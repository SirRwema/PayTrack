from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, TextInput, EmailInput
from agents.models import Agent
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.decorators import login_required

# Create your views here.

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'agent_phonenumber', 'agent_email', 'agent_location']


        widgets = {
                    'agent_name': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'agent_phonenumber': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'agent_email': EmailInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'agent_location': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                }

@login_required(login_url='/accounts/login/')           
def agent_list(request, template_name='agents/agent_list.html'):
    agents = Agent.objects.all()
    data = {}
    data['object_list'] = agents
    return render(request, template_name, data)

@login_required(login_url='/accounts/login/')
def agent_create(request, template_name='agents/agent_form.html'):
    form = AgentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('agents:agent_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def agent_update(request, pk, template_name='agents/agent_form.html'):
    agent = get_object_or_404(Agent, pk=pk)
    form = AgentForm(request.POST or None, instance=agent)
    if form.is_valid():
        form.save()
        return redirect('agents:agent_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def agent_delete(request, pk, template_name='agents/agent_delete.html'):
    agent = get_object_or_404(Agent, pk=pk)
    if request.method=='POST':
        agent.delete()
        return redirect('agents:agent_list')
    return render(request, template_name, {'object': agent})
    