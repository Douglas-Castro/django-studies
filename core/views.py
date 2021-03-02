from django.shortcuts import render
from django.contrib import messages
from .forms import contactForms


def index(request):
    return render(request, 'index.html')


def contact(request):
    form = contactForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            print('Mensagem Enviada!')
            print(f'Nome: {name}')
            print(f'E-mail: {email}')
            print(f'Assunto: {subject}')
            print(f'Mensagem: {message}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = contactForms()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form' : form
    }

    return render(request, 'contact.html', context)


def product(request):
    return render(request, 'product.html')