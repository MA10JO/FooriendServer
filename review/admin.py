from django.contrib import admin
from .models import Post, Comment, Category, Star

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nickname' : ('name',)}
admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Category, CategoryAdmin)


class StarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Star, StarAdmin)

class CommentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'nickname' : ('name',)}
admin.site.register(Comment)