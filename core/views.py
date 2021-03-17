from django.views.generic import FormView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import ContactForms, ProductModelForm
from .models import Product


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()

        return context


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForms
    success_url = reverse_lazy('contato')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')

        return super(ContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail.')

        return super(ContactView, self).form_invalid(form, *args, **kwargs)


class ProductCreate(FormView):
    template_name = 'product.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Produto Salvo!')
        print(form.cleaned_data)
        return super().form_valid(form) 

