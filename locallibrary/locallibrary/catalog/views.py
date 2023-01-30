from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic


# Create your views here.


def index(request):
    """
    Display function for the home page of the site.
    """
    # Generation of "quantities" of some main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.count()
    num_animal_books = Book.objects.all().filter(
        title__icontains='animal').count()

    # Render the HTML template index.html with data inside
    # context variable
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_animal_books': num_animal_books,
        },
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author
