from django.contrib import admin
from .models import Formation, FormationImage, FormationVideo, Video, Comment, Image

class FormationImageInline(admin.TabularInline):
    model = FormationImage
    extra = 1
    fields = ['title', 'image', ]
    
class FormationVideoInline(admin.TabularInline):
    model = FormationVideo
    extra = 1
    fields = ['title', 'video', 'views']

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "views")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description")
    inlines = [FormationImageInline, FormationVideoInline]
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at", "views")
    list_filter = ("description", "created_at")
    search_fields = ("title", "description")
   

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "created_at")
    list_filter = ("description",)
    search_fields = ("title", "description")
   

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("autor", "formation", "created_at")
    list_filter = ("created_at",)
    search_fields = ("autor", "content")
    actions = ["approve_comments", "mark_as_admin"]
    