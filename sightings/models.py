from django.db import models


class Squirrel(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
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
    shift = models.CharField(max_length=2,choices=OCCUR_TIME_CHOICES)

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

    specific_location = models.CharField(max_length=200,default=None,blank=True,null=True)

    T = 'TRUE'
    F = 'FALSE'
    SELECTION_CHOICE = [
        (T,'TRUE'),
        (F,'FALSE'),
    ]
    running = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    chasing = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    climbing = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    eating = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    foraging = models.CharField(max_length=20,choices=SELECTION_CHOICE)

    other_activities = models.CharField(max_length=200,default=None,blank=True,null=True)

    kuks = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    quaas = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    moans = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    tail_flags = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    tail_twitches = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    approaches = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    indifferent = models.CharField(max_length=20,choices=SELECTION_CHOICE)
    runs_from = models.CharField(max_length=20,choices=SELECTION_CHOICE)

    def __str__(self):
        return self.unique_squirrel_id
