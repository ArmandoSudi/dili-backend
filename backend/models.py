from django.db import models

# Create your models
class Post(models.Model):
    product_name = models.CharField(max_length=100)
    prodcut_price = models.IntegerField()
    product_description = models.CharField(max_length=250)
    post_owner_name = models.CharField(max_length=100)
    post_owner_type = (
        ('DEALER', 'Dealer'),
        ('INDIVIDUAL', 'Individual'),
    )

    def __str__(self):
        return self.product_name
