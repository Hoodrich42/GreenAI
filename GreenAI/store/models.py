from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator

class Users(models.Model):
    role_choise = [('saler', 'Продавец'),
                   ('buyer', 'Покупатель')]
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    role = models.CharField(choices=role_choise)
    def str(self):
        return self.first_name

class Category:
    category_name = models.CharField(max_length=254)
    def str(self):
        return self.category_name

class Items:
    item_name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    price = models.IntegerField()
    size = models.CharField(max_length=254)
    color = models.CharField(max_length=254)
    date_of_creation = models.DateField()
    def str(self):
        return self.item_name

class Basket:
    items = models.JSONField()
    total_cost = models.IntegerField()
    def str(self):
        return self.item

class Reviews:
    review_data = models.DateField(auto_now_add=True)
    item_name = models.CharField(max_length=254)
    description = models.TextField()
    grade = models.IntegerField(max_length=2, validators=[MinValueValidator(1), MaxValueValidator(10)])
    user = models.CharField(max_length=254)

    def str(self):
        return self.item_name