from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from shows.models import Show
from venues.models import Seat
# Create your models here.

User = get_user_model()

class Booking(models.Model):
    class BookingStatus(models.TextChoices):
        BOOKED = 'BOOKED', _('Booked')
        CANCELLED = 'CANCELLED', _('Cancelled')
        # Add other statuses if needed, e.g.
        # PENDING = 'PENDING', _('Pending')

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    seats = models.ManyToManyField(Seat, related_name='bookings')
    booked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=BookingStatus.choices,
        default=BookingStatus.BOOKED
    )

    def __str__(self):
        return f"Booking {self.pk} by {self.user.username} for {self.show.event.title} on {self.show.start_time.strftime('%Y-%m-%d %H:%M')}"