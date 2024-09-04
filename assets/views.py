from django.shortcuts import render
# assets/views.py
from django.shortcuts import render, get_object_or_404
from .models import Asset
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Asset
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Asset
from .forms import AssetForm
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('home')  # Redirect to the same page to display the success message
    else:
        form = ContactForm()

    return render(request, 'assets/home.html', {'form': form})

# def about(request):
#     return render(request, 'assets/about.html')

# def contact(request):
#     return render(request, 'assets/contact.html')


# @login_required
# def asset_list(request):
#     if request.user.is_superuser:
#         assets = Asset.objects.all()
#     else:
#         assets = Asset.objects.all()  # Adjust as necessary for regular users
#     return render(request, 'assets/asset_list.html', {'assets': assets})
from .forms import SignupForm

from django.contrib import messages
from .forms import SignupForm  # Ensure you import your form

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')  # Redirect to login page or another URL
        else:
            # Optionally add a message if the form is invalid
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignupForm()
    
    return render(request, 'assets/signup.html', {'form': form})

@login_required
def add_asset(request):
    if not request.user.is_superuser:
        return redirect('asset_list')
    
    if request.method == 'POST':
        form = AssetForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    
    return render(request, 'assets/asset_form.html', {'form': form})

@login_required
def edit_asset(request, pk):
    if not request.user.is_superuser:
        return redirect('asset_list')
    
    asset = get_object_or_404(Asset, pk=pk)
    
    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm(instance=asset)
    
    return render(request, 'assets/asset_form.html', {'form': form})

@login_required
def delete_asset(request, pk):
    if not request.user.is_superuser:
        return redirect('asset_list')
    
    asset = get_object_or_404(Asset, pk=pk)
    
    if request.method == 'POST':
        asset.delete()
        return redirect('asset_list')
    
    return render(request, 'assets/asset_confirm_delete.html', {'asset': asset})


## asset/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomLoginForm
from .models import Asset
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from .models import UserProfile


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Redirect to the Django admin page
                return redirect('/admin/')
            else:
                # Invalid credentials
                print(f"Invalid credentials for username: {username}")
                return redirect('login')
    else:
        form = CustomLoginForm()
    
    return render(request, 'assets/login.html', {'form': form})


@login_required
def admin_dashboard(request):
    # Fetch assets if needed
    assets = Asset.objects.all()
    return render(request, 'asset/admin_dashboard.html', {'assets': assets})


def user_dashboard(request):
    # Fetch assets if needed
    assets = Asset.objects.all()
    return render(request, 'asset/user_dashboard.html')

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')
def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'assets/asset_list.html', {'assets': assets})

from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def group_required(group_name):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator
from collections import defaultdict
def asset_list_view(request):
    assets = Asset.objects.all()
    totals_by_date = defaultdict(float)

    for asset in assets:
        date_str = asset.purchased_date.strftime('%Y-%m-%d')
        totals_by_date[date_str] += asset.price

    return render(request, 'assets_list.html', {
        'assets': assets,
        'totals_by_date': totals_by_date
    })
