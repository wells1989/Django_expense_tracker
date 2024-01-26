from django.db import models

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food and drink', 'Food and Drink'),
        ('bills', 'Bills'),
        ('social', 'Social'),
        ('sport', 'Sport'),
        ('misc', 'Misc'),
        # 1st value = what is displayed in the db, 2.d is what is displayed in forms etc
    ]

    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField(auto_now=True) # automatically set to current date

# old category = category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name