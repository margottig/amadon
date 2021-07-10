from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('amadon/', views.index),
    path('amadon/checkout', views.bought),
    path('checkout/<int:p_id>', views.checkout)
]
