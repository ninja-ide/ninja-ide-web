
from django.contrib.auth.models import User
from django.db import models

class NinjaProfile(models.Model):
    # ninja user profile.
    # @score would be a score/points that the user has. this
    # will let him do something in the future (not implemented yet)

    user = models.ForeignKey(User, unique=True)
    bio = models.TextField(max_length=400, blank=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
    score = models.IntegerField(default=0)

    def update_score(self):
        # looks for things this user has done, calculates the new
        # score and updates it.
        # TODO: IMPLEMENT
        pass
