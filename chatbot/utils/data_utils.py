from django.db import models

class Intent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Response(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class UserInput(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
