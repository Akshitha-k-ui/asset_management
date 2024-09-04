# assets/forms.py
from django import forms
from .models import Asset,Category

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['image','Id','name', 'description', 'quantity','price','purchased_date']



class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # user_type = forms.ChoiceField(choices=[('admin', 'Admin'), ('normal', 'Normal User')])


from django import forms
from django.contrib.auth.models import User


from django.core.validators import RegexValidator

from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    
from .models import Company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['asset', 'company_name', 'employee_name', 'address', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.all()
        self.fields['asset'].label_from_instance = lambda obj: f'{obj.Id} - {obj.name}'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['asset'].queryset = Asset.objects.all()
    #     self.fields['asset'].label_from_instance = lambda obj: f'{obj.Id} - {obj.name}'


from .models import Employee, ManagedAsset

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name', 'contact_number', 'email']

class ManagedAssetForm(forms.ModelForm):
    class Meta:
        model = ManagedAsset
        fields = ['employee', 'asset', 'bill_image', 'purchased_date', 'category_id']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.all()
        self.fields['asset'].label_from_instance = lambda obj: f'{obj.Id} - {obj.name}'   
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['employee'].queryset = Employee.objects.all()
    #     self.fields['asset'].queryset = Asset.objects.all()
    #     self.fields['category_id'].label_from_instance = lambda obj: f'{obj.category_id} - {obj.category_name}'  # Adjust based on Category model
from .models import AssetIssue
class AssetIssueForm(forms.ModelForm):
    class Meta:
        model = AssetIssue
        fields = ['asset', 'employee', 'issue_description', 'expired_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asset'].queryset = Asset.objects.all()
        self.fields['employee'].queryset = Employee.objects.all()

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

