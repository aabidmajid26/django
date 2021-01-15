from django.contrib import admin

# Register your models here.

from .models import People, Transactions

admin.site.register(People)
admin.site.register(Transactions)
