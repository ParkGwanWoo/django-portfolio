from django.contrib import admin
from .models import Portfolio
# Register your models here.

@admin.register(Portfolio)
class AdminPortfolio(admin.ModelAdmin):
    list_display = (
        'id',
        'item_title',
        'thumnail_image',
        'item_content',
        'item_link',
    )
    
    list_display_links = (
        'item_title',
        'item_content',
    )