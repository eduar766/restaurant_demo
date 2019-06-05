from django.shortcuts import render
from .models import Blog
from django.db.models import Count, Q
# Create your views here.

def search(request):
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__title=query) |
            Q(tag__title=query) 
        ).distinct()

    context = {
        'posts': queryset
    }

    return render(request, 'search_results.html', context)