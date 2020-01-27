from django.contrib import admin
from news.models import News,Category

# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    list_display_links = ("title","author")
    prepopulated_fields = {"slug": ("title",)}
    fields = ("title", ("author","category"),"content","slug","cover_image") 
    #readonly_fields = ("author",)
    exclude = ("created_at","updated_at")
    #radio_fields ={"category": admin.HORIZONTAL}
    
admin.site.register(Category)