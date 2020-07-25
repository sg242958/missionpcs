from django.db import models

class Days(models.Model):
    SEMESTER_CHOICES = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
    )
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=9, choices=SEMESTER_CHOICES, default="MONDAY")
    first = models.CharField(max_length=20, default="")
    second = models.CharField(max_length=20, default="")
    third = models.CharField(max_length=20, default="")
    fourth = models.CharField(max_length=20, default="")
    fifth = models.CharField(max_length=20, default="")
    sixth = models.CharField(max_length=20, default="")
    seventh = models.CharField(max_length=20, default="")
    eighth = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.day

    class Meta:
        verbose_name_plural = 'Days'
