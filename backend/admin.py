from django.contrib import admin

from .models import Category, Currency, Location, UserType, User, Post
from .models import PhotoURL
class CategoryAdmin(admin.ModelAdmin):
    model = Category
class CurrencyAdmin(admin.ModelAdmin):
    model = Currency
class LocationAdmin(admin.ModelAdmin):
    model = Location
class UserTypeAdmin(admin.ModelAdmin):
    model = UserType
class UserAdmin(admin.ModelAdmin):
    model = User
class PostAdmin(admin.ModelAdmin):
    model = Post
class PhotoURLAdmin(admin.ModelAdmin):
    model = PhotoURL




admin.site.register(Category, CategoryAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PhotoURL, PhotoURLAdmin)
