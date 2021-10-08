from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import CreateUserForm, CartAddProductForm
from .models import *
from .utils import cartData, guestOrder
import json
import datetime


def home(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 6)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {'products': products, 'category': category, 'categories': categories, 'cartItems': cart_items}
    return render(request, 'store/store.html', context)


def product_detail(request, id, slug):
    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']

    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {'product': product, 'cart_product_form': cart_product_form, 'items': items, 'order': order,
               'cartItems': cart_items}
    return render(request, 'store/product_detail.html', context)


def cart(request):
    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(customer=customer, order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                email = form.cleaned_data.get('email')
                Customer.objects.create(user=user, name=username, email=email)
                messages.success(request, 'Account was created for ' + username)

                to_addresses = []
                to_addresses.append(email)
                send_mail('Onyx Women & Kids Clothing', 'Dear ' + username + ',' +
                          '\n\nThank you for creating an Onyx account.To begin enjoying all the great features available to you, simply sign in with your username and password - anytime, anywhere.' +
                          '\n\nUsername: ' + username + '\n\nOnyx Women & Kids Clothing',
                          email, to_addresses)

                return redirect('login')

        context = {'form': form}
        return render(request, 'registration/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('store:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('store:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('store:home')


def contactPage(request):
    if request.method == 'POST':  # check post
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")

            to_addresses = []
            to_addresses.append(data.email)
            send_mail('Onyx Women & Kids Clothing', 'Hello ' + data.name + ',' +
                      '\n\nThank you for contacting us with your query. We will look into it and get in touch with you as soon as possible..\n\nOnyx Women & Kids Clothing',
                      data.email, to_addresses)
            return HttpResponseRedirect('/contact')

    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']

    form = ContactForm
    context = {'form': form, 'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'registration/contact.html', context)


def aboutPage(request):
    data = cartData(request)
    cart_items = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'items': items, 'order': order, 'cartItems': cart_items}
    return render(request, 'registration/about.html', context)
