from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm, Personalizado
from .forms import ContactFormForm
from django.contrib.auth.decorators import login_required

def indice(request):
    public_flans = Flan.objects.filter(is_private=False)


    return render(
        request, 
        'index.html', 
        {
            'public_flans': public_flans
        }
)


def acerca(request):
    return render(request, 'about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private=True)


    return render(
        request, 
        'welcome.html', 
        {
            'private_flans' : private_flans
        }
)

def contacto(request):
    if request.method == 'POST':

        form = ContactFormForm(request.POST)


        if form.is_valid():

            contact_form = ContactForm.objects.create(**form.cleaned_data)

            return HttpResponseRedirect('/exito')

    else:
        form = ContactFormForm()


    return render(request, 'contactus.html', {'form': form})



def exito(request):
    return render(request, 'success.html', {})


def personalizado(request):
    personalizado = Personalizado.objects.all()

    return render(
        request, 
        'personalizado.html', 
        {
            'personalizado': personalizado
        }
)






