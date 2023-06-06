from django.shortcuts import redirect, render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import *

def contact(request):
    return render(request, 'room/contact.html')

def loginPage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        users=None
        try:
            users = User.objects.get(email=email)
        except:
            messages.error(request, 'user does not not exist')

        user = authenticate(request, username=users, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist')

    return render(request, 'register/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def to_log(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        email = User.objects.all()
        new_email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if new_email not in email:
            if  password1 == password2:
                if form.is_valid():
                    user = form.save(commit=False)
                    user.email = request.POST.get('email')
                    user.save()
                    return redirect('home')
            else:
                messages.error(request, 'Error password')
            
        else:
            messages.error(request, 'this account already has been registered' )

    return render(request, 'register/to_log.html')

def home(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''
    brand = Brand.objects.all()    
    product = Product.objects.filter(
        Q(title__icontains=q) |
        Q(brand__name__icontains=q) |
        Q(description__icontains=q) 
    )
    
    context = {
        'product' : product,
        'brand' : brand,
    }
    return render(request, 'room/home.html',context)

@login_required(login_url='/login')
def addToCart(request,pk):
    products = Product.objects.get(id=pk)
    carts = Cart.objects.filter(user=request.user)
    cart_id = []
    for i in carts:
        cart_id.append(i.product.id)

    if products.id not in cart_id:
        print(cart_id)
        Cart.objects.create(
            user=request.user,
            product = products,
            price = products.price,
            quant = 1,
        )
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='/login')
def updateCart(request, pk):
    cart = Cart.objects.get(id=pk)
    quant = request.GET.get('quant')

    if request.method == 'GET' and int(quant) != 0:
        cart.quant = request.GET.get('quant')
        cart.save()
        return HttpResponseRedirect ('/mycart')
    else:
        cart.delete()
        return HttpResponseRedirect ('/mycart')


@login_required(login_url='/login')
def mycart(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for price in cart:
        total_price += price.price*price.quant

    context = {
        'cart':cart,
        'total_price':total_price,
    }

    return render(request, 'room/cart.html', context)


@login_required(login_url='/login')
def order(request):
    carts = Cart.objects.filter(user=request.user)
    for cart in carts:
        Order.objects.create(
            user = cart.user,
            product = cart.product,
            price = cart.price*cart.quant,
            quant = cart.quant
        )
        products = Product.objects.get(id=cart.product.id)
        if request.method =='GET':
            products.quant = products.quant-cart.quant
            products.save()
    carts.delete()
    return redirect('/')
    
@login_required(login_url='/login')
def myOrder(request):
    order = Order.objects.filter(user=request.user)

    context = {
        'order':order,
    }

    return render(request, 'room/order.html', context)

@login_required(login_url='/login')
def favorite(request,pk):
    products = Product.objects.get(id=pk)
    favorites = Favorite.objects.filter(user=request.user)
    fav_id = []
    for i in favorites:
        fav_id.append(i.product.id)
    if products.id not in fav_id:
        print(fav_id)
        Favorite.objects.create(
            user=request.user,
            product = products,
            price = products.price,
        )
        return redirect('/')
    else:
        return redirect('/')
    
@login_required(login_url='/login')
def myfavorite(request):
    favorite = Favorite.objects.filter(user=request.user)
    context = {
        'favorite':favorite,
    }
    return render(request, 'room/favorite.html', context)

def removeFav(request, pk):
    favorite=Favorite.objects.filter(product=pk)
    favorite.delete()
    return HttpResponseRedirect ('/myfavorite/')

def info(request,pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.filter(brand=product.brand)
    opinions = Opinion.objects.filter(product=product.id) 
    context = {
        'product':product,
        'products':products,
        'opinions':opinions,
    }
    return render(request,'room/info.html',context)       

@login_required(login_url='/login')
def create_comment(request, id):
    if request.method == "POST":
        comment = request.POST.get('comment')
        if comment and comment.strip():  
            product = Product.objects.get(id=id)
            Opinion.objects.create(
                user=request.user,
                comment=request.POST.get('comment'),
                product=product,
            )
            return redirect(f'/info/{id}')
        else:
            return redirect(f'/info/{id}')
            
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        if name and email and phone_number and message and name.strip() and email.strip() and phone_number.strip() and message.strip():
            Contact.objects.create(
                name = name,
                email = email,
                phone_number = phone_number,
                message = message,
            )
    return render(request, 'room/contact.html')
        



    