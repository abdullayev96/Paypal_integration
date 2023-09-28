from django.contrib import admin
from .models import Wallet, WalletTransaction


class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'currency', 'created_at')

    list_filter = ('full_name', 'bio')
    search_fields = ("full_name",)



admin.site.register(Wallet, WalletAdmin)
admin.site.register(WalletTransaction)
