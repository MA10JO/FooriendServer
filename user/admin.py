from django.contrib import admin
from .models import Account

# Register your models here.
@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'password',
        'name',
        'nickname',
        'phoneNum',
        'created_at',
        'updated_at'
    )
