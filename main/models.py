from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from dateutil.relativedelta import relativedelta
from datetime import date

# Create your models here.


class UserAnalysis(models.Model):
    screen_name = models.TextField(max_length=30)
    name = models.TextField(max_length=50)
    tweet_positive = models.FloatField(null=True)
    tweet_negative = models.FloatField(null=True)
    tweet_neutral = models.FloatField(null=True)
    reply_positive = models.FloatField(null=True)
    reply_negative = models.FloatField(null=True)
    reply_neutral = models.FloatField(null=True)
    follow_count = models.IntegerField(null=True)
    status_count = models.IntegerField(null=True)
    desc = models.TextField(null=True)
    profile_url = models.TextField(null=True)
    image_url = models.TextField(null=True)
    retweet_count = models.IntegerField(null=True)
    fav_count = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    username = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    mobile = models.IntegerField(max_length=15,null=True)
    address = models.TextField(default='No Address given')
    company = models.TextField(max_length=100,null=True)
    party = models.TextField(max_length=100,null=True)
    dob = models.DateField(max_length=8,null=True)
    user_type = models.CharField(max_length=30,default='Free')
    user_active = models.BooleanField(default=False)
    user_package = models.CharField(max_length=30,null=True)
    user_package_expires = models.IntegerField(max_length=10,null=True)

    def __str__(self):
        return self.username.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
