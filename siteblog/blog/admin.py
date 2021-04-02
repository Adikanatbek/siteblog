
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *
from django.utils.safestring import mark_safe

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    form = PostAdminForm

    safe_as = True
    save_on_top =True
    list_display = ('id', 'title', 'slug','category','created_at', 'get_photo')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at','get_photo')
    fields = ('title', 'slug', 'category','tags', 'content', 'photo', 'created_at', 'get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'
    get_photo.short_description = 'Фото'

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

class TAgAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TAgAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.