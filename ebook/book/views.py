from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.utils import timezone

# Create your views here.

from .forms import PostForm




def homepage(r):
    data = {}
    data['category'] = Category.objects.all()
    data['create'] = Books.objects.all()
    
    return render(r,"home.html",data)


def insert(r):
    if r.method == "POST":
        p = PostForm(r.POST,r.FILES)
        if p.is_valid():
            p.save()
        return redirect(homepage)

    return render(r,"insert.html",{"form":PostForm})


def viewPost(r,cat_id):
    data = {}
    data['category'] = Category.objects.all()
    data['create'] = Books.objects.filter(category=cat_id)
    return render(r,"home.html",data)

def search(r):
    search = r.GET.get("search")
    data = {
        "category":Category.objects.all(), 
        "create":Books.objects.filter(title__contains=search)
        }
    return render(r, "home.html",data)
  

def singlePost(r,post_id):
    data = {}
    data['category'] = Category.objects.all()
    data['show'] = Books.objects.get(pk=post_id)
   
    data['create'] = Books.objects.exclude(pk=post_id)
    return render(r,"view.html",data)

def cart(r):
    return render (r,"cart.html")

def addToCart(r,item):
    book = get_object_or_404(Books, id=item)
    orderitem, created = OrderItem.objects.get_or_create(item=book,ordered=False,user=r.user)
    order_qs = Order.objects.filter(user=r.user,ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item=book).exists():
            orderitem.qty += 1
            orderitem.save()
        else:
            order.items.add(orderitem)
    else:
        order_time = timezone.now()
        order = Order.objects.create(user=r.user, ordered_date=order_time)

        order.items.add(orderitem)
    return redirect(cart)

    
