from django.contrib import admin
from .models import Post

###admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('nengetu', 'dento', 'kuchou', 'created_date')
    ordering = ('-nengetu',)


admin.site.register(Post, PostAdmin)
