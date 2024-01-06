from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Lead(models.Model):
    # SOURCE_CHOICES = (('YouTube', 'YouTube'),
    #                   ('Google', 'Google'),
    #                   ('Newsletter', 'Newsletter'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profile_picture = models.ImageField(blank=True, null=True)
    # special_files = models.FileField()
    agent = models.ForeignKey("Agent")
