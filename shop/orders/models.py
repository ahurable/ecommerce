from django.db import models
from django.db.models.fields import related
from shop.models import Product
# Create your models here.

class Order(models.Model):

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=40)
  email = models.EmailField(max_length=120)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=30)
  postal_code = models.CharField(max_length=20)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  paid = models.BooleanField(default=False)

  def __str__(self):
    return f'order\'s {self.id}'

  def get_total_cost(self):
    return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):

  order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name="items_order", on_delete=models.CASCADE)
  price = models.DecimalField(decimal_places=1, max_digits=10)
  quantity = models.PositiveBigIntegerField(default=1)

  def __str__(self) -> str:
      return str(self.id)

  def get_cost(self):
    return self.price * self.quantity