from django.views.generic import ListView

from .models import Publisher, Book, Review


class publisher_list(ListView):
    model = Publisher
    template_name = "publisher_list.html"
    context_object_name = "publishers"
    #publishers = Publisher.objects.all()
   # return render(request, "publisher_list.html", {"publishers": publishers})

class book_list(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"
    #books = Book.objects.all()
    #return render(request, "book_list.html", {"books": books})

class review_list(ListView):
    model = Review
    template_name = "review_list.html"
    context_object_name = "reviews"
    #reviews = Review.objects.all()
    #return render(request, "review_list.html", {"reviews": reviews})