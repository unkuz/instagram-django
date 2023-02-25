from django.contrib import admin
from .models import Feed, Image, FeedImage, Video, FeedVideo, Comment, FeedComment


admin.site.register(Feed)
admin.site.register(Image)
admin.site.register(FeedImage)
admin.site.register(Video)
admin.site.register(FeedVideo)

admin.site.register(Comment)
admin.site.register(FeedComment)