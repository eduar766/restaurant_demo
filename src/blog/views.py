from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Blog
from django.db.models import Count, Q
from .forms import CommentForm

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

def blog(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'blog.html', context)


def post(request, id):
    post = get_object_or_404(Blog, id=id)
    most_recent = Blog.objects.all().order_by('-pub_date')[0:6]

    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.post = post
            form.save()
            return redirect(reverse('post', kwargs={
                'id': post.id
            }))

    context = {
        'post': post,
        'most_recent': most_recent,
        'form': form
    }
    return render(request, 'blog-details.html', context)