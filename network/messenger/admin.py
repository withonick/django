from django.contrib import admin

from messenger.models import Post, Category, Chat


# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'category', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Post, PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Chat)
