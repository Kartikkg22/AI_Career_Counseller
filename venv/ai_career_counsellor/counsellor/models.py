from django.db import models

# Create your models here.
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    interests = models.TextField()
    strengths = models.TextField(blank=True)
    tenth_score = models.FloatField()
    twelfth_score = models.FloatField()
    degree_cgpa = models.FloatField()
    skills = models.TextField()
    career_goal = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
