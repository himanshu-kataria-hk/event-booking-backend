from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookingRequestSerializer, BookingResponseSerializer
from .services import book_seats
from shows.models import Show
from django.core.exceptions import ValidationError  

class BookingView(APIView):
    def post(self, request):
        serializer = BookingRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        show_id = serializer.validated_data['show_id']
        seat_ids = serializer.validated_data['seat_ids']
        user = request.user

        try:
            show = Show.objects.get(id=show_id)
            booking = book_seats(user, show, seat_ids)
        except Show.DoesNotExist:
            return Response({"error": "Show not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An unexpected error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        response_serializer = BookingResponseSerializer(booking)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)