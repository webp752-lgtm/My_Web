from django.db import models

class ContactRequest(models.Model):

    name = models.CharField(max_length=100)

    whatsapp = models.CharField(max_length=30)

    phone = models.CharField(max_length=30)

    email = models.EmailField(
        blank=True,
        null=True
    )

    service = models.CharField(max_length=100)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class ServicesCard(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField(help_text="اكتب كل ميزة في سطر")
    active = models.BooleanField(default=True)

    def get_features(self):
        return self.features.splitlines()

    def __str__(self):
        return self.name

class SubscriptionPayment(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("verified", "Verified"),
        ("rejected", "Rejected"),
    ]

    customer_name = models.CharField(max_length=150)

    transaction_number = models.CharField(
        max_length=150
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    transfer_to = models.CharField(
        max_length=20,
        default="01023723736"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.subscription.name}"