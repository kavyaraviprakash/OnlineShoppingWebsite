from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'store'

urlpatterns = [
    # leave empty string for base url
    path('', views.home, name='home'),

    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('contact/', views.contactPage, name='contact'),
    path('about/', views.aboutPage, name='about'),

    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('<slug:category_slug>/', views.home, name='store_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
