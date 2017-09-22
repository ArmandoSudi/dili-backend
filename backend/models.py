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
