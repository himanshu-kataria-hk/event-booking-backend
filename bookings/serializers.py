from rest_framework import serializers
from .models import Booking
from venues.models import Seat
from shows.models import Show

class BookingRequestSerializer(serializers.ModelSerializer):
    show_id = serializers.IntegerField()
    seat_ids = serializers.ListField(
        child = serializers.IntegerField(),
        allow_empty = False,
    )


class BookingResponseSerializer(serializers.ModelSerializer):
    seat_ids = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id','user','seat_ids','status', 'booked_at']

    def get_seat_ids(self, obj):
        return [seat.id for seat in obj.seats.all()]