from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('login/', views.customer_login, name='customer_login'),
    # Đường dẫn trang khách hàng
    path('customer/', views.customer_home, name='customer_home'),
    # ...
]