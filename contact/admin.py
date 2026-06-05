from django.contrib import admin
from contact import models


# Register your models here.

@admin.register(models.Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone_number', 'created_date'
    ordering = '-id',
    filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_editable = 'first_name', 'last_name',
    list_per_page = 10