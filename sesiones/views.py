from django.shortcuts import render,HttpResponse
from django.views.generic.list import ListView
from .models import Books
from .forms import InputForm
from .tasks import send_book,enviar_correo

# Create your views here.
class BookList(ListView):
    model = Books
    template_name = "booklist.html"



def select_book(request, id):
    book = Books.objects.filter(bookID = int(id))
    request.session["authors"] = book[0].authors
    request.session["publication_date"] = book[0].publication_date
    
    context = {}
    context["book"] = book[0]
    context["form"]=InputForm()

    if request.method=="POST":
        form = InputForm(request.POST) #obtengo el formulario que el usuario lleno
        if form.is_valid():
            #print(form.cleaned_data['nombre']," -> ",form.cleaned_data['email'])

            #Se ejecutara la tarea para celery: 
            #send_book.delay(form.cleaned_data['nombre'],form.cleaned_data['email'])

            enviar_correo(form.cleaned_data['nombre'],form.cleaned_data['email']) #envio masivo

            return HttpResponse(form.cleaned_data['nombre']+ " -> " + form.cleaned_data['email'])

    return render(request, "oneBook.html", context)



def author(request):
    context = {}
    context["author"] = request.session["authors"]
    context["publication_date"] = request.session["publication_date"]
    
    return render(request, "author.html", context)
