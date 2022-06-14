from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    link_url = models.URLField()
    description = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def save_post(self):
        ''' method to save an image post instance '''
        self.save()

    def delete_post(self):
        '''method to delete an image post instance '''
        self.delete()

    @classmethod
    def search_project(cls, search_term):
        ''' method to search projects by title '''
        return cls.objects.filter(title__icontains=search_term).all()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    bio = models.TextField(blank=True,max_length=500) 

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Rating(models.Model):
    ''' model to allow users to rate post on three categories '''

    RATING_CHOICES = ( (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
            (6, '6'),
            (7, '7'),
            (8, '8'),
            (9, '9'),
            (10, '10'),
    )

    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    design = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability = models.IntegerField(choices=RATING_CHOICES, default=0)
    content = models.IntegerField(choices=RATING_CHOICES, default=0)
    
    def __str__(self):
        return f"{self.post}'s rating"

    def save_rating(self):
        ''' method to save ratings '''
        self.save()

    def delete_rating(self):
        ''' method to delete ratings '''
        self.delete()