from django.contrib import admin
from blog.models import BlogsPost
# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','keyword1','body','timestamp']

admin.site.register(BlogsPost,BlogsPostAdmin)

