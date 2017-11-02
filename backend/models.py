from django.db import models

# Create your models
class Post(models.Model):
    post_owner_type = (
        ('DEALER', 'Dealer'),
        ('INDIVIDUAL', 'Individual'),
    )
    product_name = models.CharField(max_length=100)
    prodcut_price = models.IntegerField()
    product_description = models.CharField(max_length=250)
    post_owner_name = models.CharField(max_length=100)
    post_image_url = models.CharField(max_length=300, default="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Ferrari_California_T_-_Mondial_de_l%27Automobile_de_Paris_2014_-_003.jpg/280px-Ferrari_California_T_-_Mondial_de_l%27Automobile_de_Paris_2014_-_003.jpg")


    def __str__(self):
        return self.product_name

class AutoPost(models.Model):
    fuel_type_choice = (
        ('DIESEL', 'Diesel'),
        ('PETROL', 'Petrol'),
        ('ELECTRIC', 'Electric'),
    )
    state_choice = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    transmission_choice = (
        ('AUTOMATIC', 'Automatic'),
        ('MANUAL', 'Manual'),
    )
    steering = (
        ('LEFT', 'Left'),
        ('RIGHT', 'Right'),
    )
    brand = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    color = models.CharField(max_length=25)
    fuel = models.CharField(max_length=10, choices=fuel_type_choice, blank=True, null=True)
    engine_size = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=10, choices=transmission_choice, blank=True, null=True)
    year_of_fabrication = models.IntegerField()
    mileage = models.IntegerField(blank=True, null=True)
    chassis = models.CharField(max_length=20, blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    exterior_color = models.CharField(max_length=25, blank=True, null=True)
    interior_color = models.CharField(max_length=25, blank=True, null=True)
    state = models.CharField(max_length=10, choices=state_choice)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.model + ' ' + self.price

class FurniturePost(models.Model):
    state_choice = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=state_choice)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.brand + ' ' + self.price

class ElectronicPost(models.Model):
    state_choice = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_of_fabrication = models.IntegerField()
    description = models.TextField()
    state = models.CharField(max_length=10, choices=state_choice, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.model + ' ' + self.brand + ' ' + price

class HousePost(models.Model):
    state_choice = (
        ('NEW', 'New'),
        ('USED', 'Used'),
    )
    house_type_choice = (
        ('FLAT', 'Flat'),
        ('INDIVIDUAL', 'Individual'),
        ('BUILDING', 'Building'),
    )
    house_service_type_choice = (
        ('SALE','Sale'),
        ('RENT','Rent'),
    )
    address = models.CharField(max_length=250)
    bedroom = models.IntegerField()
    Hall = models.IntegerField()
    bathroom = models.IntegerField()
    parking = models.IntegerField()
    swimming_pool = models.BooleanField()
    house_service_type = models.CharField(max_length=20, choices=house_service_type_choice)
    house_type = models.CharField(max_length=20, choices=house_type_choice)
    state = models.CharField(max_length=10, choices=state_choice)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.address + ' ' + self.price

class LawnPost(models.Model):
    address = models.CharField(max_length=250)
    length = models.IntegerField()
    width = models.IntegerField()
    price = models.IntegerField()

class JobAndServicePost(models.Model):
    type_choice = (
        ('JOB','Job'),
        ('SERVICE','Service'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    #duration

    def __str__(self):
        return self.title + ' ' + self.price
