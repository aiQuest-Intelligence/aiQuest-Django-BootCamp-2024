from django.shortcuts import render,redirect
from django.views import View 
from .models import Customer, Product, Cart , OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class ProductView(View):
    def get(self, request):
        totalitem = 0
        all_product = Product.objects.all()
        vegetable= Product.objects.filter(category='VEG')
        fruit= Product.objects.filter(category='FR')
        juice= Product.objects.filter(category='JU')
        teacofee = Product.objects.filter(category='TC')
        bread = Product.objects.filter(category='BRD')
        if request.user.is_authenticated:
             totalitem = len(Cart.objects.filter(user=request.user))
        return render(request,'home/home-4.html',{'all_product': all_product,'vegetable': vegetable,'fruit':fruit,'juice': juice,'teacofee':teacofee,'bread':bread,'totalitem':totalitem})
    

class ProductDetailView(View):
	def get(self, request, pk):
		totalitem = 0
		product = Product.objects.get(pk=pk)
		print(product.id)
		item_already_in_cart=False
		if request.user.is_authenticated:
			totalitem = len(Cart.objects.filter(user=request.user))
			item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
		return render(request, 'product_details/product-details.html', {'product':product, 'item_already_in_cart':item_already_in_cart, 'totalitem':totalitem})
    
@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product= Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    print(product)
    return redirect('/cart')


@login_required
def show_cart(request):
	totalitem = 0
	if request.user.is_authenticated:
		totalitem = len(Cart.objects.filter(user=request.user))
		user = request.user
		cart = Cart.objects.filter(user=user)
		amount = 0.0
		shipping_amount = 70.0
		totalamount=0.0
		cart_product = [p for p in Cart.objects.all() if p.user == request.user]
		print(cart_product)
		if cart_product:
			for p in cart_product:
				tempamount = (p.quantity * p.product.discounted_price)
				amount += tempamount
			totalamount = amount+shipping_amount
			return render(request, 'cart/addtocart.html', {'carts':cart, 'amount':amount, 'totalamount':totalamount, 'totalitem':totalitem})
		else:
			return render(request, 'cart/emptycart.html', {'totalitem':totalitem})
	else:
		return render(request, 'cart/emptycart.html', {'totalitem':totalitem})


def plus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity+=1
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Cart.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

def minus_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.quantity-=1
		c.save()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Cart.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'quantity':c.quantity,
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")

def remove_cart(request):
	if request.method == 'GET':
		prod_id = request.GET['prod_id']
		c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
		c.delete()
		amount = 0.0
		shipping_amount= 70.0
		cart_product = [p for p in Cart.objects.all() if p.user == request.user]
		for p in cart_product:
			tempamount = (p.quantity * p.product.discounted_price)
			# print("Quantity", p.quantity)
			# print("Selling Price", p.product.discounted_price)
			# print("Before", amount)
			amount += tempamount
			# print("After", amount)
		# print("Total", amount)
		data = {
			'amount':amount,
			'totalamount':amount+shipping_amount
		}
		return JsonResponse(data)
	else:
		return HttpResponse("")                



def vegetable(request,data=None):
    if data== None:
        vegetables = Product.objects.filter(category='VEG')
    elif data == 'Tomato' or data== 'Fulkopy':
        vegetables = Product.objects.filter(food_brand= data) 
    return render(request,'vegetable/product_vegetable.html',{'vegetables':vegetables})
        
def fruit(request,data=None):
    if data== None:
        fruits = Product.objects.filter(category='FR')
    elif data == 'Banana' or data== 'Apple':
        fruits = Product.objects.filter(food_brand= data) 
    return render(request,'fruits/product_fruits.html',{'fruits':fruits})

def juice(request,data=None):
    if data== None:
        juices = Product.objects.filter(category='JU')
    elif data == 'Apple Juice' or data== 'Tomato Juice':
        juices = Product.objects.filter(food_brand= data) 
    return render(request,'juice/product_juice.html',{'juices':juices})

def tea(request,data=None):
    if data== None:
        teas = Product.objects.filter(category='TC')
    elif data == 'Tea' or data== 'Tea Black':
        teas = Product.objects.filter(food_brand= data) 
    return render(request,'tea/product_tea.html',{'teas':teas})

def bread(request,data=None):
    if data== None:
        breads = Product.objects.filter(category='BRD')
    elif data == 'Brown Bread' or data== 'White Bread':
        breads = Product.objects.filter(food_brand= data) 
    return render(request,'bread/product_bread.html',{'breads':breads})

def jam(request,data=None):
    if data== None:
        jams = Product.objects.filter(category='JAM')
    elif data == 'Apple Jam' or data== 'Orange Jam':
        jams = Product.objects.filter(food_brand= data) 
    return render(request,'jam/product_jam.html',{'jams':jams})  

def product_grid(request):
    all_products = Product.objects.all()
    return render(request,'product_details/product-grid-left-sidebar.html',{'all_products':all_products})


@login_required
def checkout(request):
	user = request.user
	add = Customer.objects.filter(user=user)
	cart_items = Cart.objects.filter(user=request.user)
	amount = 0.0
	shipping_amount = 70.0
	totalamount=0.0
	cart_product = [p for p in Cart.objects.all() if p.user == request.user]
	if cart_product:
		for p in cart_product:
			tempamount = (p.quantity * p.product.discounted_price)
			amount += tempamount
		totalamount = amount+shipping_amount
	return render(request, 'product_details/checkout.html', {'add':add, 'cart_items':cart_items, 'totalcost':totalamount})

@login_required
def orders(request):
	op = OrderPlaced.objects.filter(user=request.user)
	return render(request, 'cart/orders.html', {'order_placed':op})

@login_required
def payment_done(request):
	custid = request.GET.get('custid')
	print("Customer ID", custid)
	user = request.user
	cartid = Cart.objects.filter(user = user)
	customer = Customer.objects.get(id=custid)
	print(customer)
	for cid in cartid:
		OrderPlaced(user=user, customer=customer, product=cid.product, quantity=cid.quantity).save()
		print("Order Saved")
		cid.delete()
		print("Cart Item Deleted")
	return redirect("orders")
       
      
def blog(request):
    return render(request,'blog/blog-detail.html')

def about(request):
    return render(request,'about/page-about-us.html')

def contact(request):
    return render(request,'contact/page-contact.html')

@login_required
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'profile/address.html',{'add':add,'active':'btn-primary'})


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'login/customer_registration.html',{'form':form})
    
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations!! registered Successfully')     
            form.save()
        return render(request,'login/customer_registration.html',{'form':form})        


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile/profile.html',{'form':form,'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']             
            locality = form.cleaned_data['locality']             
            city = form.cleaned_data['city']             
            zipcode = form.cleaned_data['zipcode']             
            district= form.cleaned_data['district']
            reg= Customer(user=usr, name=name, locality=locality, city=city, district=district, zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile Update Succcessfully')
        return render(request,'profile/profile.html',{'form':form,'active':'btn-primary'})                 
         