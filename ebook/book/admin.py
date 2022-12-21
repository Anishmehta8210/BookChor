from django.contrib import admin
from book.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Payment)
admin.site.register(Address)
