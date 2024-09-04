from django.db import models
# assets/models.py
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

from datetime import datetime
class Asset(models.Model):
    Id=models.CharField(max_length=100,default='')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price=models.CharField(max_length=100,default='')
    purchased_date=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='assets/images/', blank=True, null=True)
    
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='companies')
    asset_id = models.CharField(max_length=100, blank=True, null=True) 
    company_name = models.CharField(max_length=255)
    employee_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.company_name
    
    def save(self, *args, **kwargs):
        if self.asset:
            self.asset_id = self.asset.Id  # Automatically populate asset_id
        super().save(*args, **kwargs)
    
    @property
    def asset_id(self):
        return self.asset.Id
    
    @property
    def asset_name(self):
        return self.asset.name if self.asset else 'Unknown'

    

   
    class Meta:
        permissions = [
            ("can_add_asset", "Can add asset"),
            ("can_delete_asset", "Can delete asset"),
            ("can_change_asset", "Can change asset"),
            ("can_view_asset", "Can view asset"),
            ("can_approve_asset", "Can approve asset"),  # Custom permission example
        ]


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=[('admin', 'Admin'), ('normal', 'Normal User')])

    def __str__(self):
        return self.user.username

# # Create a profile automatically when a new user is created
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
# post_save.connect(create_user_profile, sender=User)

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('office', 'Office'),
        ('lab', 'Lab'),
        ('classroom', 'Classroom'),
        ('sports', 'Sports'),
        ('others', 'Others'),
    ]

    # asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='categories')
    category_id = models.CharField(max_length=100, default='')
    category_name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'{self.category_name} '


class Employee(models.Model):
    emp_id = models.CharField(max_length=100, unique=True)
    emp_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.emp_name
    
class ManagedAsset(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='managed_assets')
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='managed_assets')
    bill_image = models.ImageField(upload_to='managed_assets/bills/', blank=True, null=True)
    purchased_date = models.DateField(default=datetime.now)
    category_id = models.CharField(max_length=100)  # Assuming you have category_id or a related Category model

    def __str__(self):
        return f'{self.employee.emp_name} - {self.asset.name}'
    

class AssetIssue(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='issues')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    issue_description = models.TextField()
    expired_date = models.DateField()

    def __str__(self):
        return f"Issue with {self.asset} reported by {self.employee}"

from django.db.models import Sum
class TotalAsset(models.Model):
    total_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Total Asset Amount: {self.total_amount}"

    @classmethod
    def update_total_amount(cls):
        total_value = Asset.objects.aggregate(total=Sum('value'))['total'] or 0.00
        obj, created = cls.objects.get_or_create(id=1)
        obj.total_amount = total_value
        obj.save()

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    

