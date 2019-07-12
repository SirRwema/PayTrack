from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from cashdrops.models import Cashdrop
from django.contrib.auth.decorators import login_required

# Create your views here.

class CashdropForm(ModelForm):
    class Meta:
        model = Cashdrop
        fields = ['id', 'slug', 'position', 'delivery_location', 'delivered_to', 'date_of_delivery', 'delivery_amount', 'rate', 'delivery_agent', 'sent_by', 'status', 'remarks']

@login_required(login_url='/accounts/login/')
def cashdrop_list(request, template_name='cashdrops/cashdrop_list.html'):
    cashdrops = Cashdrop.objects.all()
    data = {}
    data['object_list'] = cashdrops
    return render(request, template_name, data)

@login_required(login_url='/accounts/login/')
def cashdrop_create(request, template_name='cashdrops/cashdrop_form.html'):
    form = CashdropForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cashdrops:cashdrop_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def cashdrop_update(request, pk, template_name='cashdrops/cashdrop_form.html'):
    cashdrop = get_object_or_404(Cashdrop, pk=pk)
    form = CashdropForm(request.POST or None, instance=cashdrop)
    if form.is_valid():
        form.save()
        return redirect('cashdrops:cashdrop_list')
    return render(request, template_name, {'form':form})

@login_required(login_url='/accounts/login/')
def cashdrop_delete(request, pk, template_name='cashdrops/cashdrop_delete.html'):
    cashdrop = get_object_or_404(Cashdrop, pk=pk)
    if request.method=='POST':
        cashdrop.delete()
        return redirect('cashdrops:cashdrop_list')
    return render(request, template_name, {'object': cashdrop})
    