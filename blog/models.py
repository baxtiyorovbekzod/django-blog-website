from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(default=now)
    views = models.PositiveIntegerField(default=0)
    reading_minute = models.PositiveIntegerField(default=5)
    tg_link = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title