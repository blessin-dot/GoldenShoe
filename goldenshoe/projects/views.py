import email
from importlib.metadata import requires
from itertools import product
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Basket, Project
from .forms import ProjectForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

basket_items = []

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    if request.method == "POST":
        messages.success(request, "Email has been sent successfully")
        return redirect('projects')
    return render(request, 'projects/index.html', context)

def shoes(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/shoes_list.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.info(request, 'Username or Password not correct. Try again...')
    context = {}
    return render(request, 'projects/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'You have successfully registered')
            return redirect('login')
    context = {'form': form}
    return render(request, 'projects/register.html', context)

@login_required(login_url='login')
def refund(request):
    refund_message = "Thanks for your enquiry. Your refund will be soon processed. Find attached the return label"
    context = {}
    if request.method == "POST":
        order_id = request.POST.get('order_number')
        reason = request.POST.get('return_reason')
        email_address = request.POST.get('email_address')

        # print(request.user)
        # send_mail('Golden Shoe Refund Request',refund_message, email_address, [email_address], fail_silently=False)
        messages.success(request, "Email has been sent! your refund request is in process")
        context = {'order_id': order_id, 'reason_id': reason}
        return render(request, 'projects/confirmation_refund.html', context)
    return render(request, 'projects/refund_form.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk)
    form = ProjectForm(request.POST)
    context = {'form': form}
    
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, instance=projectObject)
        if form.is_valid():
            form.save()
            print("it's valid")
            return redirect('projects')
    context = {'form': form, 'project': projectObject}
    return render(request, 'projects/single_project.html', context)

def view_basket(request):
    return render(request,'projects/basket.html')

def add_basket(request, pk):
    project = Project.objects.get(id=pk)
    form =  ProjectForm(instance=project)
    form = ""
    total = 0

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            quantity = form.cleaned_data.get("shoe_quantity")
            size = form.cleaned_data.get("shoe_size")
            price = round(project.price * quantity, 2)
            basket = Basket(basket_quantity=quantity, basket_value=price)
            basket.save()
            basket_items.append(basket)
            print(basket.basket_quantity)
            print(basket.basket_value)
            print(basket_items)
            print(type(quantity))
            print(type(size))
            new_stock_quantity = project.stock_quantity - quantity
            if new_stock_quantity < 0:
                new_stock_quantity = 0
            print(Project.objects.filter(id=pk).update(shoe_quantity=quantity))
            print(Project.objects.filter(id=pk).update(stock_quantity=new_stock_quantity))
            for item in basket_items:
                total += item.basket_value
    context = {'form': form, 'basket': basket_items, 'product': project, 'total': round(total, 2)}
    print(context)
    return render(request, 'projects/basket.html', context)

def clear_basket(request):
    basket_items[:] = []
    context={'basket': [], 'product': []}
    return render(request, 'projects/basket.html', context)

def checkout(request):
    total = 0
    if request.method == "POST":
        card_details = request.POST.get('card_details')
        delivery_address = request.POST.get('delivery_address')
        messages.success(request, 'Payment went through. The order has been placed')
        basket_items[:] = []
        return redirect('projects')
    for item in basket_items:
        total += item.basket_value
    context = {'basket': basket_items, 'total': total}
    return render(request, 'projects/checkout.html', context)


def info_page(request):
    return render(request, 'projects/info.html')



