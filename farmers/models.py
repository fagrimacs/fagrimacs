from uuid import uuid4

from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


# Farmer Profile
def profile_pic_filename(instance, filename):
    ext = filename.split('.')[1]
    new_filename = '{}.{}'.format(uuid4(), ext)
    return f'profile_pics/{new_filename}'


class FarmerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    profile_pic = models.ImageField(verbose_name='Profile Picture', default='profile_pics/default.png', upload_to=profile_pic_filename)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.name} Profile'

    def get_absolute_url(self):
        return reverse('farmer:farmer-profile', kwargs={'pk': self.user_id})

    def get_profile_update_url(self):
        return reverse('farmer:farmer-profile-update', kwargs={'pk': self.user_id})
