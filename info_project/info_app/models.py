from django.db import models
from django.contrib.auth.models import User 
from PIL import Image
from django.urls import reverse


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)

class FederalRegister(models.Model):
    title = models.CharField(max_length=500, primary_key=True, unique=True)
    description = models.TextField(max_length=500, null=True)
    pubDate = models.DateField(null=True)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('federalregister-detail', kwargs={'pk': self.pk})
