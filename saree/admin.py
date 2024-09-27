from django.contrib import admin 
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)

admin.site.register(Supplier)
admin.site.register(SupplierContract)
admin.site.register(CommunicationHistory)
admin.site.register(Seller)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['fullname', 'address', 'postal_code']



class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at', 'comment')
    list_filter = ('product', 'user', 'rating', 'created_at')
    search_fields = ('comment', 'user__username', 'product__name')


admin.site.register(Review, ReviewAdmin)
