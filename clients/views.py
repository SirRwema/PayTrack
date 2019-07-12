from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from clients.models import Clients

# Create your views here.

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['id', 'slug', 'client_name', 'client_phonenumber', 'client_email', 'client_location']

def client_list(request, template_name='clients/client_list.html'):
    clients = Clients.objects.all()
    data = {}
    data['object_list'] = clients
    return render(request, template_name, data)

def client_create(request, template_name='clients/client_form.html'):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clients:client_list')
    return render(request, template_name, {'form':form})

def client_update(request, pk, template_name='clients/client_form.html'):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients:client_list')
    return render(request, template_name, {'form':form})

def client_delete(request, pk, template_name='clients/client_delete.html'):
    client = get_object_or_404(Client, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('clients:client_list')
    return render(request, template_name, {'object': client})
    