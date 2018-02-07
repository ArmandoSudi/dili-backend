from django.contrib import admin

from .models import Post, AutoPost, FurniturePost, ElectronicPost, HousePost, LawnPost, JobAndServicePost
from .models import PhotoURL

class PostAdmin(admin.ModelAdmin):
    model = Post

class AutoPostAdmin(admin.ModelAdmin):
    model = AutoPost

class PhotoURLAdmin(admin.ModelAdmin):
    model = PhotoURL

class FurniturePostAdmin(admin.ModelAdmin):
    model = FurniturePost

class ElectronicPostAdmin(admin.ModelAdmin):
    model = ElectronicPost

class HousePostAdmin(admin.ModelAdmin):
    model = HousePost

class HousePostAdmin(admin.ModelAdmin):
    model = HousePost

class LawnPostAdmin(admin.ModelAdmin):
    model = LawnPost

class JobAndServicePostAdmin(admin.ModelAdmin):
    model = JobAndServicePost

admin.site.register(Post, PostAdmin)
admin.site.register(AutoPost, AutoPostAdmin)
admin.site.register(FurniturePost, FurniturePostAdmin)
admin.site.register(ElectronicPost, ElectronicPostAdmin)
admin.site.register(HousePost, HousePostAdmin)
admin.site.register(LawnPost, LawnPostAdmin)
admin.site.register(JobAndServicePost, JobAndServicePostAdmin)
admin.site.register(PhotoURL, PhotoURLAdmin)
