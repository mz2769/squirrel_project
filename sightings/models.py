from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(
        max_length=200,
        unique=True,
        primary_key=True,
    )

    Morning = 'AM'
    Afternoon = 'PM'
    OCCUR_TIME_CHOICES = [
        (Morning,'AM'),
        (Afternoon,'PM'),
    ]
    shift = models.CharField(
        max_length=2,
        choices=OCCUR_TIME_CHOICES,
        default=Morning,
    )

    date = models.DateField()

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AGE_CHOICES = [
        (Adult,'Adult'),
        (Juvenile,'Juvenile'),
    ]
    age = models.CharField(
        max_length=20,
        choices=AGE_CHOICES,
        default=None,
        blank=True,
        null=True,
    )

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    COLOR_CHOICES = [
        (Gray,'Gray'),
        (Cinnamon,'Cinnamon'),
        (Black,'Black'),
    ]
    primary_fur_color = models.CharField(
        max_length=20,
        choices=COLOR_CHOICES,
        default=None,
        blank=True,
        null=True,
    )

    A = 'Ground Plane'
    B = 'Above Ground'
    LOCATION_CHOICES = [
        (A,'Ground Plane'),
        (B,'Above Ground'),
    ]
    location = models.CharField(
        max_length=40,
        choices=LOCATION_CHOICES,
        default=None,
        blank=True,
        null=True,
    )

    specific_location = models.CharField(
        max_length=200,
        default=None,
        blank=True,
        null=True,
    )

    T = 'TRUE'
    F = 'FALSE'
    SELECTION_CHOICE = [
        (T,'TRUE'),
        (F,'FALSE'),
    ]
    running = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    chasing = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    climbing = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    eating = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    foraging = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )

    other_activities = models.CharField(
        max_length=200,
        default=None,
        blank=True,
        null=True,
    )

    kuks = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    quaas = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    moans = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    tail_flags = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    tail_twitches = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    approaches = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    indifferent = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    runs_from = models.CharField(
        max_length=20,
        choices=SELECTION_CHOICE,
        default=F,
    )
    def __str__(self):
        return self.unique_squirrel_id
