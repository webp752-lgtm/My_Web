from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('company/', views.company, name='company'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path("contact/", views.contact, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),
    path('', views.login_view, name='login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name='logout'),
    path("subscriptions/",views.subscriptions,name="subscriptions"),
    path("subscriptions/payment/<int:pk>/",views.subscription_payment,name="subscription_payment"),
    path("portfolio/",views.portofolio,name="portfolio"),
]
