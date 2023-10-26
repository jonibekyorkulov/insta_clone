from django.contrib import admin
from .models import Post, PostComment, PostLike, CommentLike
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'caption', 'created_time')
    search_fields = ('id', 'author__username', 'caption')
    readonly_fields = ('id',)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_time')
    search_fields = ('id', 'author__username', 'comment')
    readonly_fields = ('id',)


class PostLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'created_time')
    search_fields = ('id', 'author__username')
    readonly_fields = ('id',)


class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'created_time')
    search_fields = ('id', 'author__username')
    readonly_fields = ('id',)


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostLike, PostLikeAdmin)
admin.site.register(CommentLike, CommentLikeAdmin)
