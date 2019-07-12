from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from agents.models import Agent
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.decorators import login_required

# Create your views here.

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['id', 'slug', 'agent_name', 'agent_phonenumber', 'agent_email', 'agent_location']


        
        #agent_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'inlineFormInput',  'class':'form-control mb-2'}))
        #agent_phonenumber = forms.CharField(widget=forms.TextInput(attrs={'id': 'inlineFormInput',  'class':'form-control mb-2'}))
        #agent_email = forms.CharField(widget=forms.TextInput(attrs={'id': 'inlineFormInput',  'class':'form-control mb-2'}))
        #agent_location = forms.CharField(widget=forms.TextInput(attrs={'id': 'inlineFormInput',  'class':'form-control mb-2'}))

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
    