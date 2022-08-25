from audioop import reverse
from email.mime import image
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from django.utils import timezone
from django.urls import reverse


class Post(Model):
    title = models.CharField(max_length=255, null=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(default=timezone.now)
    image = models.ImageField(default='default.webp', upload_to='post_image/')
    
    def __str__(self):
        return f'{self.title} '

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
