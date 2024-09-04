# assets/admin.py
from django.contrib import admin
from .models import Asset,Employee, ManagedAsset
from django.utils.html import format_html

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('image_thumbnail','Id','name', 'description', 'quantity','price','purchased_date', 'created_at', 'updated_at',)
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<a href="{}" target="_blank">'
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover;"/>'
                '</a>',
                obj.image.url,
                obj.image.url
            )
        return "No Image"
    
    image_thumbnail.short_description = 'Image Preview'

# from django.contrib import admin
# from django.contrib.auth.models import User
# from .models import UserProfile

# class UserAdmin(admin.ModelAdmin):
#     # Specify fields to display
#     list_display = ('username', 'email', 'first_name', 'last_name', 'user_type_display')

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         # Ensure that the user profile exists
#         try:
#             user_profile = request.user.userprofile
#             if user_profile.user_type == 'normal':
#                 # Normal users should only see themselves or have limited access
#                 return qs.filter(id=request.user.id)
#         except UserProfile.DoesNotExist:
#             pass
#         return qs

#     def user_type_display(self, user):
#         # Display the user type if it exists
#         try:
#             return user.userprofile.user_type
#         except UserProfile.DoesNotExist:
#             return 'No Profile'

#     user_type_display.short_description = 'User Type'

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# from django.contrib.auth.models import Group
# class MyAdminSite(admin.AdminSite):
#     def has_permission(self, request):
#         if not request.user.is_authenticated:
#             return False
#         if request.user.is_superuser:
#             return True
#         return False  # Default behavior

# admin_site = MyAdminSite(name='myadmin')
# admin_site.register(Group)
# from .models import companyinfo
# admin.site.register(companyinfo)
from .models import Asset, Company,Category
from .forms import CompanyForm

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ('company_name', 'employee_name', 'address', 'email', 'phone_number', 'asset_id', 'asset_name')
    search_fields = ('company_name', 'employee_name', 'address', 'email', 'phone_number', 'asset_id', 'asset__Id', 'asset__name')
    list_filter = ('asset_id', 'asset__Id', 'asset__name')  # Filter by Asset ID and other related fields

    def asset_id(self, obj):
        return obj.asset.Id

    asset_id.short_description = 'Asset ID'

    def asset_name(self, obj):
        return obj.asset_name

    asset_name.short_description = 'Asset Name'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name')
    search_fields = ('category_id', 'category_name')
    list_filter = ('category_name','category_id')

    def category_id(self, obj):
        return obj.category_id

    category_id.short_description = 'Category ID'




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'contact_number', 'email')
    search_fields = ('emp_id', 'emp_name', 'contact_number', 'email')
    

@admin.register(ManagedAsset)
class ManagedAssetAdmin(admin.ModelAdmin):
    list_display = ('employee','asset_id', 'asset_name', 'bill_image', 'purchased_date', 'category_id')
    search_fields = ('employee__emp_name',  'category_id','asset_id', 'asset__Id', 'asset__name')
    list_filter = ('employee', 'asset_id', 'asset__Id', 'asset__name', 'purchased_date', 'category_id')

    def asset_id(self, obj):
        return obj.asset.Id

    asset_id.short_description = 'Asset ID'

    def asset_name(self, obj):
        return obj.asset.name

    asset_name.short_description = 'Asset Name'

from .models import AssetIssue

@admin.register(AssetIssue)
class AssetIssueAdmin(admin.ModelAdmin):
    list_display = ('asset', 'employee', 'issue_description', 'expired_date')
    search_fields = ('asset__Id', 'employee__first_name', 'employee__last_name', 'issue_description')
    list_filter = ('asset', 'employee', 'expired_date')

    def asset_id(self, obj):
        return obj.asset.Id

    asset_id.short_description = 'Asset ID'

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','message', 'created_at')


