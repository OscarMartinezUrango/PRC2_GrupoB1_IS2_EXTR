from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'destinations.html', { 'destinations': all_destinations})

# Nos formalizamos todo lo necesario para las opniniones que nos sugieren en el enunciado de la practica
def Opiniones(request):
    all_reviews = models.Opinion.objects.all()
    return render(request, 'Opiniones.html', {'opiniones': all_reviews})

class CrearOpinion(SuccessMessageMixin, generic.CreateView):
    model = models.Opinion
    template_name = 'opinion_formulario.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('opiniones') 
    success_message = 'La opinión "%(name)s" ha sido creada con éxito.'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class ActualizarOpinion(generic.UpdateView):
    model = models.Opinion
    template_name = 'opinion_formulario.html'
    fields = ['name','description']


class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'

class CruiseDetailView(generic.DetailView):
    template_name = 'cruise_detail.html'
    model = models.Cruise
    context_object_name = 'cruise'

 # CAMBIOS PARA MANDAR EL EMAIL CON EL INFO REQUEST
class InfoRequestCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'info_request_create.html'
    model = models.InfoRequest
    fields = ['name', 'email', 'cruise', 'notes']
    success_url = reverse_lazy('index')
    success_message = 'Email confirmation successful'

    def form_valid(self, form):
        subject = 'Confirmation of InfoRequest'
        message = render_to_string('email.html', {'name': form.cleaned_data['name'], 'cruise': form.cleaned_data['cruise']})
        plain_message = strip_tags(message)
        from_email = 'grupob1is2extr@gmail.com'
        to_email = form.cleaned_data['email']
        send_mail(subject, plain_message, from_email, [to_email], html_message=message)
        return super().form_valid(form)