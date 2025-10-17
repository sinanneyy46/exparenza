from django.db import models


class Result(models.Model):
    event_name = models.CharField(max_length=255)
    zone = models.CharField(max_length=100, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_name} - {self.zone}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='gallery/')
    published = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"
    

class Headline(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='headlines/')
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def short_content(self):
        # for preview cards
        return self.content[:100] + '...' if len(self.content) > 100 else self.content

