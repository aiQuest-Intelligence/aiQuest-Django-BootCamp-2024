from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

DISTRICT_CHOICE = (
    ('Dhaka','Dhaka'),
    ('Chattogram','Chattogram'),
    ('Khulna','Khulna'),
    ('Rajshahi','Rajshahi'),
    ('Shylet','Shylet'),
    ('Rangpur','Rangpur'),
    ('Barishal','Barishal'),
    ('Maymansing','Maymansing'),
)
class Customer(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    district = models.CharField(choices = DISTRICT_CHOICE, max_length=50)
    
    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
    ('VEG','Vegetable'),
    ('BRD','Bread'),
    ('FR','Fruits'),
    ('JU','Juice'),
    ('TC','Teacoffee'),
    ('JAM','Jam'),
    ('SF','SeaFood'),
    ('FMT','FreshMeats'),
)

STOCK_CHOICE = (
    ('STOCK IN','STOCK IN'),
    ('STOCK OUT','STOCK OUT'),
)

class Product(models.Model):
    title = models.CharField(max_length = 100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    basic_description = models.TextField()
    description = models.TextField()
    additional_information = models.TextField()
    food_brand = models.CharField(max_length=100)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=3)
    stock = models.CharField(choices = STOCK_CHOICE,max_length=40)
    product_1_image = models.ImageField(upload_to='productimg')
    product_2_image = models.ImageField(upload_to='productimg')
    product_3_image = models.ImageField(upload_to='productimg')
    product_4_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)        

    def __str__(self):
        return str(self.id)
    # Below Property will be used by checkout.html page to show total cost in order summary
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)    

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices = STATUS_CHOICES, max_length=50,default='Pending')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price




