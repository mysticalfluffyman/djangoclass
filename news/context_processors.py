from django.shortcuts import render
from news.models import Category


def categories(request):
    categories_list = Category.objects.all()
    return{"categories": categories_list} 