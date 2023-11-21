from django.contrib import admin
from .models import Post,Category,Comments


# custimize admin panel
class Postadmin(admin.ModelAdmin):
    list_display=['title','draft']
    list_filter=['title','draft','author']
    search_fields=['title']
# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Comments)
