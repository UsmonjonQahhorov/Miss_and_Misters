from django.urls import path

from apps.orders.views import OrderCreateView, OrderListView, OrderUpdateView, OrderDeleteView

urlpatterns = [
    path('order/create/', OrderCreateView.as_view()),
    path('order/list/', OrderListView.as_view()),
    path('order/update/<int:pk>/', OrderUpdateView.as_view()),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view()),
]
