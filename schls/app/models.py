from django.db import models

# Create your models here.
class coursedetails(models.Model):
    name=models.CharField(max_length=10)
    durations=models.CharField(max_length=10)
    fees=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Applymodel(models.Model):
        COURSE_CHOICES = [
        ('python', 'Python Full Stack'),
        ('java', 'Java Full Stack'),
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
    ]
        
        name=models.CharField(max_length=10)
        
        passyear=models.CharField(max_length=10)
        phone=models.CharField(max_length=10)
        email=models.CharField(max_length=10)
        selectcourse = models.CharField(max_length=50, choices=COURSE_CHOICES)
        def __str__(self):
            return self.name