from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import InterestingFactsForm
from .models import InterestingFacts


def news_home(request):
    news = InterestingFacts.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = InterestingFacts
    template_name = 'news/detail_view.html'
    context_object_name = 'fact'




class NewsUpdateView(UpdateView):
    model = InterestingFacts
    template_name = 'news/create.html'
    form_class = InterestingFactsForm

class NewsDeleteView(DeleteView):
    model = InterestingFacts
    success_url='/news'
    template_name = 'news/news_delete.html'




def create(request):
    error = ''
    if request.method == 'POST':
        form = InterestingFactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не верная"
    form = InterestingFactsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

# Create your views here.
