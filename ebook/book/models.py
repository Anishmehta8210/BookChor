from django.db import models
from django.conf import settings

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=200)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_title

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    isbn = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    image = models.ImageField(upload_to="images/",null=True,blank=True)

    def __str__(self):
        return self.title

class OrderItem(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
     ordered = models.BooleanField(default=False)
     item = models.ForeignKey(Books,on_delete=models.CASCADE)
     qty = models.IntegerField(default=1)

     def __str__(self):
         return self.user.username
     

ADDRESS_TYPE = (
    ("H", "Home"),
    ("O", "Office"),
)

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    pincode = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    address_type = models.CharField(max_length=200,choices=ADDRESS_TYPE)
    default = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    

class Coupon(models.Model):
    code = models.CharField(max_length=200)
    amount = models.FloatField()

    def __str__(self):
        return self.code
    

class Payment(models.Model):
    txn_id = models.CharField(max_length=400)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    

class Order (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=200,null=True,blank=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField(null=True,blank=True)
    address = models.ForeignKey(Address,on_delete=models.SET_NULL,null=True,blank=True)
    ordered = models.BooleanField(default=False)
    payment = models.ForeignKey(Payment,on_delete=models.SET_NULL,null=True,blank=True)
    coupon = models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True,blank=True)
    being_delivered = models.BooleanField(default=False)
    recieved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
