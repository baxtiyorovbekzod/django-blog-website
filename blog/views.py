from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView # Djangoning tayyor kutubxonalari
from .models import Post # O'zingiz yaratgan model

# 1. Asosiy sahifa uchun View (Faqat oxirgi 2 ta post)
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Bazadan faqat e'lon qilingan va oxirgi 2 ta postni oladi
        return Post.objects.filter(is_published=True).order_by('-published_date')[:2]


# 2. Barcha bloglar ro'yxati va Qidiruv uchun View
class BlogsView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Default holatda hamma postlarni oladi
        queryset = Post.objects.filter(is_published=True).order_by('-published_date')
        
        # Qidiruv so'rovi kelgan bo'lsa, filtrlash
        query = self.request.GET.get('search')
        if query:
            queryset = queryset.filter(title__icontains=query)
        
        return queryset


# 3. Blogning batafsil sahifasi uchun View
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug' # URL'dagi slug orqali postni topadi

    def get_object(self):
        # Post ko'rilganda views sonini +1 ga oshirish
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj