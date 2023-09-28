from django.contrib import admin
from .models import Payment



class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'amount', 'order_id', 'razorpay_payment_id', 'paid']
    search_fields = ['name']


admin.site.register(Payment, PaymentAdmin)

