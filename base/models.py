from django.db import models


class FileAnalyzer(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField()
    to_do = models.TextField()
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} analyzer"