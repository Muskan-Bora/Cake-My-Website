from django.db import models
from django.contrib.auth.models import User
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType
# from food.models import AllCategories

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.png',upload_to='profile_pictures')
    location = models.CharField(default='Location',max_length=100)
    user_type = models.CharField(max_length=200, default='user_type')

    def __str__(self):
        return self.user.username
    
class ItemPictures(models.Model):
    name = models.CharField(default='itemname', max_length=50)
    pictures = models.ImageField(default='item_pic.jpg', upload_to='item_pictures')

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to user
    cake_id = models.PositiveIntegerField(default=0)  # Generic ID for any cake, default is 0
    cake_category = models.CharField(max_length=50, default="generic_cake")  # Default category
    net_weight = models.PositiveIntegerField(default=250)  # Default weight is 250gm
    quantity = models.PositiveIntegerField(default=1)  # Default quantity is 1
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default price is $0.00
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Default total price is $0.00

    def save(self, *args, **kwargs):
        # Ensure total price is calculated before saving
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.cake_category} - {self.cake_id} - {self.quantity} items"