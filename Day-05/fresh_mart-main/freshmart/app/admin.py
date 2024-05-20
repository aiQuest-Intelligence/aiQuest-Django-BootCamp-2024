from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','district']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','basic_description','description','additional_information','food_brand','category','stock','product_1_image','product_2_image','product_3_image','product_4_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['user','customer','product','quantity','ordered_date','status']
    


    
    
    
    
    
    
    
    
    
    
        

