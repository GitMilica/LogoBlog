from django.contrib import admin
from .models import Post, Author
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("date",)
    list_display = ("title", "date",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
