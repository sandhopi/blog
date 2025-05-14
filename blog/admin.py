from django.contrib import admin

# Register your models here.
from .models import ContentBlog, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta :
        model = Category

@admin.register(ContentBlog)
class PostContentBlogAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]
    class Meta :
        model = ContentBlog