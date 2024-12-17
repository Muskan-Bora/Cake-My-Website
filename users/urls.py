from django.urls import path

from users import views
app_name = 'users'

urlpatterns = [
    path('cart/add/', views.add_to_cart, name='add_to_cart'),  # Add to cart
    path('cart/', views.view_cart, name='view_cart'),  # View cart
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
]

