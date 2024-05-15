from django.shortcuts import render,get_object_or_404,redirect
from .models import Book

from .forms import BookForm
# Create your views here.
from django.http import HttpResponse

def index(request):
    queryset = Book.objects.all()
    context={"books":queryset}
    return render(request, "index.html",context=context)
def detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'detail.html', {'book': book})
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
