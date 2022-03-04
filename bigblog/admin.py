from django.contrib import admin
from .models import  Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	lsit_filter = ("status", "created", "publish", "author")
	search_fields = ('title',  'body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = "publish"
	ordering  = ['status', 'publish'] 

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
# Register your models here.
