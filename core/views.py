from django.shortcuts import render
from django.contrib import messages
from .forms import contactForms, ProductModelForm


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = contactForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.sendMail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = contactForms()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form' : form
    }

    return render(request, 'contact.html', context)


def product(request):
    if str(request.method) == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto Salvo com Sucesso!')
            form = ProductModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProductModelForm()
    
    context = {
        'form': form
    }

    return render(request, 'product.html', context)