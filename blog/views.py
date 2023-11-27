from django.shortcuts import render, get_object_or_404
from .models import Blog, Page

def about_me(request):
    return render(request, 'blog/about_me.html')

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def page_list(request):
    pages = Page.objects.all()
    if not pages:
        return render(request, 'blog/no_pages.html')

    return render(request, 'blog/page_list.html', {'pages': pages})

def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'blog/page_detail.html', {'page': page})

def page_not_found(request, exception):
    return render(request, 'blog/page_not_found.html', status=404)