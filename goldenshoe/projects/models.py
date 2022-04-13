from email.policy import default
from pyexpat import model
from sys import set_coroutine_origin_tracking_depth
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import uuid
from  django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# in the relationship many-to-many, we use the tag in quotes because the class definition is below
# the actual class. Otherwise, if it was above the class, we wouldn't need the tags

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    time_created = models.DateTimeField(auto_now_add=True)
    shoe_size = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(4), MaxValueValidator(12)])
    shoe_quantity = models.IntegerField(default=0, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    stock_quantity = models.IntegerField(default=0, null=True, validators=[MinValueValidator(0)])
    price = models.FloatField(default=0.00, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    def get_model_fields(model):
        return model._meta.fields


class Basket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    order_id = models.IntegerField(default=0)
    basket_quantity = models.IntegerField(default=0, blank=True, null=True)
    basket_value = models.FloatField(default=0.00, null=True)
    prodcut_id = models.CharField(max_length=500)
    product_name = models.CharField(max_length=500)

    def __str__(self):
	    return str(self.id)
