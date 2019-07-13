from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm, TextInput, EmailInput, DateInput, NumberInput, Select
from cashdrops.models import Cashdrop
from django.contrib.auth.decorators import login_required

# Create your views here.


class CashdropForm(ModelForm):
    class Meta:
        model = Cashdrop
        fields = ['id','delivery_location', 'receiver', 'date_of_delivery', 'delivery_amount', 'rate', 'delivery_agent', 'sent_by', 'status']
        widgets = {
                    'delivery_location': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'receiver': TextInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'date_of_delivery': DateInput(attrs={'class': 'form-control', 'id': 'example-date', 'type':'date'}),
                    'delivery_amount': NumberInput(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'rate': Select(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'delivery_agent': Select(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'sent_by': Select(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'}),
                    'status': Select(attrs={'class': 'form-control mb-2', 'id': 'inlineFormInput'})
                }

@login_required(login_url='/accounts/login/')
def counters(request, template_name='cashdrops/cashdrop_list.html' ):
    total_cashdrops = Cashdrop.objects.count()
    pending_cashdrops = Cashdrop.objects.filter(status = 'pending').count()
    complete_cashdrops = Cashdrop.objects.filter(status = 'complete').count()
    cancelled_cashdrops = Cashdrop.objects.filter(status = 'cancelled').count()
    context = { 'total_cashdrops': total_cashdrops,
                'pending_cashdrops':pending_cashdrops,
                'complete_cashdrops':complete_cashdrops,
                'cancelled_cashdrops':cancelled_cashdrops }
    return render(request, template_name , context)

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
    