from django.db import models
from events.models import Event
from venues.models import Screen

class Show(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    language = models.CharField(max_length=50, blank=True, null=True)  # Optional field for language
    format = models.CharField(max_length=20, blank=True, null=True)  # Optional field for format (e.g., 2D, 3D)

    class Meta:
        unique_together = ('screen', 'start_time')

    def __str__(self):
        return f"{self.event.title} at {self.screen.name} on {self.start_time.strftime('%Y-%m-%d %H:%M')}"