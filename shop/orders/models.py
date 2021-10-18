from django.db import models
from django.db.models.fields import related
from shop.models import Product
# Create your models here.

class BillingInformation(models.Model):

  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  ship_address = models.CharField(max_length=250)
  postal_code = models.CharField(max_length=20)
  state = models.CharField(max_length=30)
  city = models.CharField(max_length=30)





class Order(models.Model):

  bills = models.ForeignKey(BillingInformation, related_name="bills", on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self)->str:
    return f"order id {self.id}"

  # total cost function will get the price of whole items in cart
  def total_cost(self):
    # self.items refers to order attribute in OrderItem Model
    return sum(item.get_cost for item in self.items)


class OrderItem(models.Model):

  order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
  items = models.ForeignKey(Product, related_name="items_order", on_delete=models.CASCADE)
  price = models.DecimalField(decimal_places=1, max_digits=10)
  quantity = models.PositiveBigIntegerField(default=1)

  def __str__(self) -> str:
      return str(self.id)

  def get_cost(self):
    return self.price * self.quantity