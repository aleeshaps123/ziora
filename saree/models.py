from django.db import models
from django.contrib.auth.models import AbstractUser,User
from django.utils import timezone  # Make sure to import timezone

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='productimages/')
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    reorderlevel = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default='Uncategorized')
    created_at = models.DateTimeField(auto_now_add=True)

    def is_at_reorder_level(self):
        return self.quantity == self.reorderlevel

    def __str__(self):
        return self.name

from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from textblob import TextBlob

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # Ensure rating is between 1 and 5
    )
    created_at = models.DateTimeField(default=timezone.now)
    sentiment = models.CharField(max_length=10, blank=True)  # New field for sentiment

    def save(self, *args, **kwargs):
        self.sentiment = self.analyze_sentiment()
        super().save(*args, **kwargs)

    def analyze_sentiment(self):
        analysis = TextBlob(self.comment)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    def __str__(self):
        return f'Review by {self.user} on {self.product}'



class UserProfile(AbstractUser):
    # Add any additional fields you need here
    age = models.PositiveIntegerField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)  # Nullable email field
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_profiles',  # Custom related name to avoid clashes
        related_query_name='user_profile',
        blank=True,
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart for {self.user.username}: {self.product.name}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),

    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    fullname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    phone_number= models.CharField(max_length=13,default='')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.fullname} placed on {self.created_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in order {self.order.id}"


from django.db import models

class Supplier(models.Model):
    
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class SupplierContract(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='contracts', on_delete=models.CASCADE)
    contract_details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Contract with {self.supplier.name} from {self.start_date} to {self.end_date}"

class CommunicationHistory(models.Model):
    supplier = models.ForeignKey(Supplier, related_name='communications', on_delete=models.CASCADE)
    communication_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"Communication with {self.supplier.name} on {self.communication_date}"


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


# models.py

class PurchaseOrder(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)  # Added seller field
    
    quantity = models.PositiveIntegerField()
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order {self.id} - {self.product.name}'

    def accept_order(self):
        self.order_status = 'Accepted'
        self.product.quantity += self.quantity
        self.product.save()
        self.save()

    def reject_order(self):
        self.order_status = 'Rejected'
        self.save()