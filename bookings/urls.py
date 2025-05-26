from django.urls import path
from .views import BookingView

urlpatterns = [
    path('book/', BookingView.as_view(), name='book-seats'),
]
