from django import forms
from .models import Product,UserProfile,Cart


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image','category','quantity', 'reorderlevel']

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'confirm_password']
        
class UserProfileForm(forms.ModelForm):
   
    class Meta:
        model = UserProfile
        fields = [ 'username','first_name', 'last_name', 'email','profile_picture']
   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'quantity']

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
from django import forms
from .models import Supplier, SupplierContract, CommunicationHistory

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_name', 'phone', 'email', 'address']

class SupplierContractForm(forms.ModelForm):
    class Meta:
        model = SupplierContract
        fields = ['supplier', 'contract_details', 'start_date', 'end_date']

class CommunicationHistoryForm(forms.ModelForm):
    class Meta:
        model = CommunicationHistory
        fields = ['supplier', 'details']

from django import forms
from django.contrib.auth.models import User
from .models import Seller

class SellerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            self.add_error('password_confirm', 'Passwords do not match')

        return cleaned_data

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ['created_at']


from django import forms
from .models import PurchaseOrder, Seller

class PurchaseOrderForm(forms.ModelForm):
    seller = forms.ModelChoiceField(queryset=Seller.objects.all())

    class Meta:
        model = PurchaseOrder
        fields = ['product', 'seller',  'quantity', 'order_status']
from django import forms
from .models import PurchaseOrder

class PurchaseOrderUpdateForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['order_status']

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5})
        }


