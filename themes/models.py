from django.db import models

# Model for themes
class SiteSetting(models.Model):
    banner=models.ImageField(upload_to='mediaa/site/')
    caption=models.TextField()
