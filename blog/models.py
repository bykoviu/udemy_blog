from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='event_images')
    text = models.TextField()
    date = models.DateTimeField()

    def get_summary(self):
        return self.text[:60]


