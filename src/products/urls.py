



from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view, social_view
from .views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
    )


app_name = 'product'
urlpatterns = [
	path('create/', product_create_view),
    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),

]
