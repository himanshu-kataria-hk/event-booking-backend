from django.db import models
from django.utils.translation import gettext_lazy as _ # For internationalization

# Create your models here.
class Event(models.Model):

    class EventType(models.TextChoices):
        MOVIE = 'movie', _('Movie')
        CONCERT = 'concert', _('Concert')
        SPORTS = 'sports', _('Sports')
        PLAY = 'play', _('Play')
        WORKSHOP = 'workshop', _('Workshop')
        # If you wanted a choice like 'OTHER' and let Django auto-generate the label:
        # OTHER = 'other' # Django would make the label 'Other'

    title = models.CharField(max_length=255)
    event_type = models.CharField(
        max_length=10, # Ensure this is long enough for your longest choice value
        choices=EventType.choices,
        # default=EventType.MOVIE # Optional: good practice to set a default
    )
    description = models.TextField()
    duration = models.DurationField()
    poster = models.ImageField(upload_to='posters/')

    def __str__(self):
        return f"{self.title} ({self.get_event_type_display()})"
