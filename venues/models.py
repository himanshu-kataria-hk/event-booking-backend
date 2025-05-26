from django.db import models
from django.utils.translation import gettext_lazy as _ # For internationalization

class Venue(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.name}, {self.city}"
    
class Screen(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='screens')
    name = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f"{self.name} at {self.venue.name}"
    
class Seat(models.Model):
    class SeatType(models.TextChoices):
        VIP = 'VIP', _('VIP')
        REGULAR = 'REGULAR', _('Regular')
        # Add more seat types as needed, e.g.:
        # PREMIUM = 'PREMIUM', _('Premium')

    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=2) # Consider if 'AA' or longer rows are possible
    number = models.PositiveIntegerField()
    seat_type = models.CharField(
        max_length=10, # Ensure this is long enough for your longest choice value (e.g., 'REGULAR')
        choices=SeatType.choices,
        default=SeatType.REGULAR # Optional: good practice to set a default
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['screen', 'row', 'number'], name='unique_seat_in_screen')
        ]

    def __str__(self):
        return f"{self.get_seat_type_display()} Seat {self.row}{self.number} at {self.screen.name}"