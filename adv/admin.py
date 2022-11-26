from django.contrib import admin
from .models import Post, Comment, Category, State, Account

# Register your models here.
admin.site.register(Account)

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)


class StateAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(State, StateAdmin)

admin.site.register(Comment)