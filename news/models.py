from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#Django-ORM (Object Relational Mapping)

class Category (models.Model):
    title = models.CharField(max_length=30 )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title




class News(models.Model):
    
    title = models.CharField(max_length=225)
    content = models.TextField()
    count = models.IntegerField(default=0)
    category = models.ManyToManyField(Category,related_name="news_categories")
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover_image = models.ImageField(upload_to="news",null=True)
    slug = models.SlugField(max_length=255,null=True)

    def get_absolute_url(self):
        return reverse("single_news", kwargs={"pk": self.pk,"slug":self.slug})
    