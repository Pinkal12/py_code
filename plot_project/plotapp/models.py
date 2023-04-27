from django.db import models

class Anomaly(models.Model):
    ANOMALY_TYPE_CHOICES = [
        ('pothole', 'Pothole'),
        ('patch', 'Patch'),
        ('webcrack', 'Webcrack'),
    ]

    anomaly_number = models.IntegerField()
    anomaly_type = models.CharField(max_length=8, choices=ANOMALY_TYPE_CHOICES)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    length = models.DecimalField(max_digits=6, decimal_places=4)
    width = models.DecimalField(max_digits=6, decimal_places=4)
    area = models.DecimalField(max_digits=9, decimal_places=4)
    size = models.CharField(max_length=16)
    distance = models.DecimalField(max_digits=6, decimal_places=4)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Anomaly {self.anomaly_number}: {self.anomaly_type}"