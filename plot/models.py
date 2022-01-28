from django.db import models

class Plot(models.Model):
    class Meta:
        permissions = [
            ("access_plot", "Have access to plots")
        ]