from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'views')
    prepopulated_fields = {'slug': ('title',)} # Titleni yozsangiz, slug o'zi yoziladi