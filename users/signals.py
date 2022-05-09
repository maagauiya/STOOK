from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile

def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user = instance,
            username = instance.username
        )
        print('profile created')
        
def update_profile(sender, instance, created, **kwargs):
    user_profile, _ = UserProfile.objects.get_or_create(user=instance)
    if created == False:
        user_profile.username = instance.username
        user_profile.save()
        print('profile updated')
        
post_save.connect(create_profile, sender=User)
post_save.connect(update_profile, sender=User)