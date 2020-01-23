from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import (
    TemplateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    CreateView,
) 
from news.models import Category, News
from news.forms import NewsCreateForm

# Create your views here.
class CategoryNewsView(View):
    def get(self, request, category_id, *args, **kwargs):
        template_name = "news/categories.html"
        #category =  Category.objects.get(pk=category_id)
        category = get_object_or_404(Category, pk=category_id)
        category_news_list = News.objects.filter(category=category) 
        popular=News.objects.order_by("-count")[:4]
        return render(request,template_name,{"category_news_list": category_news_list, "category" : category,"popular_news" : popular})

class NewsTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        category_news_list = {}
        for category in categories:
            category_news_list[category] = News.objects.filter(category=category)
        context["slider_news"]= News.objects.all()
        context["news_list"] = News.objects.all().order_by("-created_at")[:4]
        context["category_news_list"] = category_news_list
        context["popular_news"]= News.objects.order_by("-count")[:4] 
        
        return context
    
class NewsDetail(DetailView):
    model= News
    template_name = "news/single_news.html"
    context_object_name = "detail_news"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.count = self.object.count + 1
        self.object.save()
        context["popular_news"]= News.objects.order_by("-count")[:4] 
        print(context)
        return context


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = News
    template_name = "news/create.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")
    form_class = NewsCreateForm

    def form_valid(self, form):
        news = form.save(commit=False)
        title = form.cleaned_data["title"]
        slug = slugify(title)
        news.slug = slug
        news.author = self.request.user
        news.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class NewsUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = "news/update.html"
    fields = "title", "content", "cover_image", "category"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")



class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return self.post(self, request, *args, **kwargs)
    

    