from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Books


# Create your views here.
class BookList(ListView):
    model = Books
    template_name = "booklist.html"



def select_book(request, id):
    book = Books.objects.filter(bookID = id)
    request.session["authors"] = book[0].authors
    request.session["publication_date"] = book[0].publication_date
   
    context = {}
    context["book"] = book[0]
    return render(request, "oneBook.html", context)



def author(request):
    context = {}
    context["author"] = request.session["authors"]
    context["publication_date"] = request.session["publication_date"]
    
    return render(request, "author.html", context)
