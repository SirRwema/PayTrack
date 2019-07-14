from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.decorators import login_required
from clients.models import Clients
from cashdrops.models import Cashdrop


# Create your views here.

class ClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ('id', 'client_name','client_personnel', 'client_phonenumber', 'client_email', 'client_location')
        widgets = {
                    'client_name': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'client_personnel': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'client_phonenumber': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'client_email': EmailInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'client_location': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                }


total_cashdrops = Cashdrop.objects.count()
pending_cashdrops = Cashdrop.objects.filter(status = 'Pending').count()
complete_cashdrops = Cashdrop.objects.filter(status = 'Complete').count()
cancelled_cashdrops = Cashdrop.objects.filter(status = 'Cancelled').count() 


@login_required(login_url='/login/')
def client_list(request, template_name='clients/client_list.html'):
    clients = Clients.objects.all()
    context = {
            'clients':clients,
            'total_cashdrops': total_cashdrops,
            'pending_cashdrops':pending_cashdrops,
            'complete_cashdrops':complete_cashdrops,
            'cancelled_cashdrops':cancelled_cashdrops  
    }
    return render(request, template_name, context)

@login_required(login_url='/login/')
def client_create(request, template_name='clients/client_form.html'):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clients:client_list')
    context = {
            'form':form,
            'total_cashdrops': total_cashdrops,
            'pending_cashdrops':pending_cashdrops,
            'complete_cashdrops':complete_cashdrops,
            'cancelled_cashdrops':cancelled_cashdrops  
    }
    return render(request, template_name, context)

@login_required(login_url='/login/')
def client_update(request, pk, template_name='clients/client_form.html'):
    client = get_object_or_404(Client, pk=pk)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('clients:client_list')
    context = {
            'form':form,
            'total_cashdrops': total_cashdrops,
            'pending_cashdrops':pending_cashdrops,
            'complete_cashdrops':complete_cashdrops,
            'cancelled_cashdrops':cancelled_cashdrops  
    }
    return render(request, template_name, context)

@login_required(login_url='/login/')
def client_delete(request, pk, template_name='clients/client_delete.html'):
    client = get_object_or_404(Client, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('clients:client_list')
    context = {
            'object':client,
            'total_cashdrops': total_cashdrops,
            'pending_cashdrops':pending_cashdrops,
            'complete_cashdrops':complete_cashdrops,
            'cancelled_cashdrops':cancelled_cashdrops  
    }
    return render(request, template_name, context)
    