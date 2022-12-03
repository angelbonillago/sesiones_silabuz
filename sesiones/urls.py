from django.urls import path
from django.views.decorators.cache import cache_page
from . import views
from .views import BookList,select_book,author


urlpatterns = [
   #path('', ),
    path("sesiones/libro/", cache_page(60*15)(views.BookList.as_view()), name="BookList"),
    #url(r'^$', cache_page(60*60)(BookList.as_view()), name="index"),
    
    path("sesiones/select/<int:id>",select_book,name="selectbook"),

    path("sesiones/mostrar-autor",author,name="author")
    
]
