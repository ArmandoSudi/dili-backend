from django.db import models
from django.utils.timezone import now

class Category(models.Model):
    label = models.CharField(max_length=250)
    parent_category = models.ForeignKey('self',null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.label

class Currency(models.Model):
    iso_code = models.CharField(max_length=3)
    label = models.CharField(max_length=250)

    def __str__(self):
        return self.label

class Location(models.Model):
    label = models.CharField(max_length=250)

    def __str__(self):
        return self.label

class UserType(models.Model):
    label = models.CharField(max_length=250)

    def __str__(self):
        return self.label

class User(models.Model):
    user_uid = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    user_type = models.ForeignKey(UserType, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    avatar_url = models.URLField()
    
    def __str__(self):
        return self.name + ": " + self.email + ": " + self.phone_number

# Make the location field optional by adding blank=True
# Make 0 the default for the field views
class Post(models.Model):
    product_brand = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    prodcut_price = models.IntegerField()
    product_description = models.CharField(max_length=250)
    thumbnail_url = models.URLField(blank=True, null=True, default="http://via.placeholder.com/140x100")
    publication_date = models.DateTimeField(blank=True, null=True,default=now)
    views = models.IntegerField(default=0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    latitude = models.DecimalField(decimal_places=2, max_digits=5, null=True, default=0.0)
    longitude = models.DecimalField(decimal_places=2, max_digits=5, null=True, default=0.0)
    location = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.product_model + " - " + self.product_brand + ": " + str(self.prodcut_price)

class PhotoURL(models.Model):
    url = models.URLField()
    post_id = models.IntegerField()

    def __str__(self):
        return str(self.url)
