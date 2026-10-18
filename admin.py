from django.contrib import admin
from .models import ContactRequest
from .models import ServicesCard
from .models import Subscription


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "whatsapp",
        "phone",
        "email",
        "service",
        "created_at",
    )

    search_fields = (
        "name",
        "whatsapp",
        "phone",
        "email",
    )

    list_filter = (
        "service",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

@admin.register(ServicesCard)
class ServicesCardAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'text')
    ordering = ('number',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "active",
    )

    list_filter = (
        "active",
    )