from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactRequest
from .models import ServicesCard
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Subscription
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        whatsapp = request.POST.get("whatsapp")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        service = request.POST.get("service")
        message = request.POST.get("message")

        ContactRequest.objects.create(
            name=name,
            whatsapp=whatsapp,
            phone=phone,
            email=email,
            service=service,
            message=message
        )

        return redirect("contact_success")

    return render(request, "contact.html")

def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(
                request,
                'Username or password is incorrect.'
            )

    return render(request, 'login.html')


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            messages.error(
                request,
                'Passwords do not match.'
            )

            return render(
                request,
                'register.html'
            )

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Username already exists.'
            )

            return render(
                request,
                'register.html'
            )

        if email and User.objects.filter(email=email).exists():

            messages.error(
                request,
                'Email already exists.'
            )

            return render(
                request,
                'register.html'
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'register.html')


def logout_view(request):

    logout(request)

    return redirect('home')

def contact_success(request):
    return render(request, "contact_success.html")

def company(request):
    return render(request, 'company.html')

def landing_page(request):
    return render(request, 'landing_page.html')
def subscriptions(request):
    plans = Subscription.objects.filter(active=True)

    return render(request, "subscriptions.html", {
        "plans": plans
    })


def subscription_payment(request, pk):
    plan = get_object_or_404(
        Subscription,
        pk=pk,
        active=True
    )

    return render(request, "subscription_payment.html", {
        "plan": plan
    })


def services(request):
    services_cards = ServicesCard.objects.all()

    return render(request, 'services.html', {
        'services_cards': services_cards
    })

def portofolio(request):
    return render(request, 'portofolio.html')