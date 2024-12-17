from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    rest_owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1',
    )
    prod_code = models.IntegerField(default=50)
    added_by = models.CharField(
        max_length=50,
        default='user',
    )
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(
        max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla! Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur? Iusto architecto et nesciunt earum adipisci illum!')
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125"
    )
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.item_name

# -------------------------------------------------------------------

class Trending(models.Model):
    trend_code = models.IntegerField(default=50)
    trend_name = models.CharField(max_length=100)
    trend_image = models.ImageField(
        upload_to='trending cakes',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    trend_type = models.CharField(
        max_length=50,
        default = 'trend'
    )

    def __str__(self):
        return self.trend_name

# ---------------------------------------------------------------------
    
class Designing(models.Model):
    design_code = models.IntegerField(default=50)
    design_name = models.CharField(max_length=100)
    design_image = models.ImageField(
        upload_to='designing cakes',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    design_type = models.CharField(
        max_length=50,
        default = 'design'
    )

    def __str__(self):
        return self.design_name

# ------------------------------------------------------------------------------
class Desserts(models.Model):
    dessert_code = models.IntegerField(default=50)
    dessert_name = models.CharField(max_length=100)
    dessert_image = models.ImageField(
        upload_to='desserts',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    dessert_type = models.CharField(
        max_length=50,
        default = 'desserts'
    )

    def __str__(self):
        return self.dessert_name
    
# ---------------------------------------------------------------------------

CATEGORIES = {
    ('EC', 'Eggless Cakes'),
    ('GC', 'Gourmet Cakes'),
    ('PC', 'Photo Cakes'),
    ('HC', 'Heart-Shaped Cakes'),
    ('Wed', 'Wedding Cakes'),
    ('GH', 'Gift Hampers'),
    ('TC', 'Tea Cakes & Cookies')
}

class Category(models.Model):
    category_code = models.IntegerField(default=20)
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(
        max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.')
    category_price = models.IntegerField()
    category_image = models.ImageField(
        upload_to = 'category',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125' 
    )
    categories = models.CharField(choices=CATEGORIES, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.category_name
    
# -----------------------------------------------------------------

FLAVOUR = {
    ('CC', 'Chocolate Cakes'),
    ('FC', 'Fruit Cakes'),
    ('RC', 'Red Velvet Cakes'),
    ('SC', 'Strawberry Cakes'),
    ('BC', 'Blackforest Cakes'),
    ('PC', 'Pineapple Cakes'),
    ('BSC', 'Butterscotch Cakes'),
}

class Flavour(models.Model):
    flavour_code = models.IntegerField(default=30)
    flavour_name = models.CharField(max_length=100)
    flavour_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    flavour_price = models.IntegerField()
    flavour_image = models.ImageField(
        upload_to='flavour',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    flavour = models.CharField(choices=FLAVOUR, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.flavour_name


KIDS = {
    ('PC', 'Princess Cakes'),
    ('CC', 'Car Cakes'),
    ('CTC', 'Cartoon Cakes'),
    ('SHC', 'SuperHero Cakes'),
}

class Kids(models.Model):
    kids_code = models.IntegerField(default=30)
    kids_name = models.CharField(max_length=100)
    kids_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    kids_price = models.IntegerField()
    kids_image = models.ImageField(
        upload_to='kids',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    kids = models.CharField(choices=KIDS, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.kids_name

TRENDING = {
    ('PC', 'Pinata Cakes'),
    ('BC', 'Bomb Cakes'),
    ('PMC', 'Pull Me Up Cakes'),
    ('SCB', 'Suprise Cake Box'),
}

class Trend(models.Model):
    tending_code = models.IntegerField(default=40)
    trending_name = models.CharField(max_length=100)
    trending_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    trending_price = models.IntegerField()
    trending_image = models.ImageField(
        upload_to='trending',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    trending = models.CharField(choices=TRENDING, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    category = models.CharField(max_length=100, default='name of model')

    def __str__(self):
        return self.trending_name

OCCASION = {
    ('MFC', 'Mothers & Fathers Day Cakes'),
    ('DC', 'Doctors Dya Cake'),
    ('TC', 'Teachers Day Cake'),
}

class Occasional(models.Model):
    occasion_code = models.IntegerField(default=50)
    occasion_name = models.CharField(max_length=100)
    occasion_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    occasion_price = models.IntegerField()
    occasion_image = models.ImageField(
        upload_to='occasion',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    occasion = models.CharField(choices=OCCASION, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.occasion_name

DESIGNING = {
    ('ANC', 'Alphabet & Number Cakes'),
    ('BSC', 'Baby Shower Cakes'),
    ('CTC', 'Cricket Theme Cakes'),
    ('JTC', 'Jungle Theme Cakes'),
}

class Design(models.Model):
    designing_code = models.IntegerField(default=60)
    designing_name = models.CharField(max_length=100)
    designing_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    designing_price = models.IntegerField()
    designing_image = models.ImageField(
        upload_to='designing',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    designing = models.CharField(choices=DESIGNING, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.designing_name

BIRTHDAY = {
    ('BPC', 'Birthday Photo Cakes'),
    ('BC', '1st Birthday Cakes'),
    ('SBC', 'Special Birthday Cakes'),
}

class Birthday(models.Model):
    birthday_code = models.IntegerField(default=70)
    birthday_name = models.CharField(max_length=100)
    birthday_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    birthday_price = models.IntegerField()
    birthday_image = models.ImageField(
        upload_to='birthday',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    birthday = models.CharField(choices=BIRTHDAY, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.birthday_name

ANNIVERSARY = {
    ('APC','Anniversary Photo Cakes'),
    ('1AC', '1st Anniversary Cakes'),
    ('25A', '25th Anniversary Cakes'),
    ('50A', '50th Anniversary Cakes'),
}

class Anniversary(models.Model):
    anniversary_code = models.IntegerField(default=80)
    anniversary_name = models.CharField(max_length=100)
    anniversary_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    anniversary_price = models.IntegerField()
    anniversary_image = models.ImageField(
        upload_to='anniversary',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    anniversary = models.CharField(choices=ANNIVERSARY, max_length=3)
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.anniversary_name

DESSERT = {
    ('PS', 'Pastries'),
    ('JC', 'Jar Cakes'),
    ('CC', 'Cup Cakes'),
    ('BN', 'Brownies'),
}

class Dessert_Cake(models.Model):
    dc_code = models.IntegerField(default=90)
    dc_name = models.CharField(max_length=100)
    dc_desc = models.CharField(
    max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    dc_price = models.IntegerField()
    dc_image = models.ImageField(
        upload_to='dessert_cake',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    dessert_cake = models.CharField(choices=DESSERT, max_length=3)
    dessert_price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    dessert_price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    dessert_price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.dc_name
    
class AllCategories(models.Model):
    ac_code = models.IntegerField(default=90)
    ac_name = models.CharField(max_length=100)
    ac_desc = models.CharField(
        max_length=500,
        default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Dolore natus dolorum nulla. Ut placeat fuga iure dolor voluptates velit asperiores nemo voluptatem pariatur. Iusto architecto et nesciunt earum adipisci illum.'
    )
    ac_price = models.IntegerField()
    ac_image = models.ImageField(
        upload_to='allcategory_cake',
        default='https://www.thatlittlecakeshop.co.nz/cdn/shop/products/E6A577FE-B2BE-4ED2-B9BD-17041EE271EC.jpg?v=1630311125'
    )
    price_250gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_500gm = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )
    price_1kg = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        default='10.5'
    )

    def __str__(self):
        return self.ac_name