from django.contrib import admin
from blog.models import BlogsPost,IMG
# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title','keyword1','body','timestamp']

admin.site.register(BlogsPost,BlogsPostAdmin)
admin.site.register(IMG)


