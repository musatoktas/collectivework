import os
from django.contrib.auth.models import User
from django.db import models


from collectivework import settings

def get_image_path(instance, filename):
    return os.path.join(settings.MEDIA_URL, 'images', str(instance.user.id), filename )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=45)
    profile_photo = models.ImageField(upload_to=)
        upload_to = get_image_path(
            upload_to=get_image_path,
            blank=True,
            null=True,
        )