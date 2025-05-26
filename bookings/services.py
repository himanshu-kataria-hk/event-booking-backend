from django.db import transaction
from django.db.models import Q
from django.core.exceptions import ValidationError
from bookings.models import Booking
from venues.models import Seat

def book_seats(user, show, seat_ids):
    seats = Seat.objects.filter(id__in=seat_ids).select_for_update()

    with transaction.atomic():
        conflicts = Booking.objects.filter(
            show=show,
            seats__in=seats
        ).exists()
        if conflicts:
            raise ValidationError("One or more seats are already booked for this show.")
        
        booking = Booking.objects.create(user=user, show=show)
        booking.seats.set(seats)
        return booking