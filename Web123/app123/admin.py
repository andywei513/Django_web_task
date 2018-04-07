from django.contrib import admin

# Register your models here.

from .models import Article,User

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','url','body','create_date']

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(Article,ArticleAdmin)

admin.site.register(User,UserAdmin)
