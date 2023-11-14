from django.db import models
from django.contrib.auth.models import User

# User is a built-in model in django.contrib.auth.models

# Default User model has the following fields:
# username, password, email, first_name, last_name (all CharField)
# alredy defined in django.contrib.auth.models which will be accessed  by OneToOneField
# we just need to add additional fields to the User model


# Here we create a new model UserProfileInfo which inherits from models.Model class

class UserProfileInfo(models.Model):
    # create a one-to-one relationship with User model which stores the default fields of User model
    user= models.OneToOneField(User, on_delete=models.CASCADE)

    # additional fields
    portfolio_site = models.URLField(blank=True) # blank=True means this field is not required
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) # upload_to='profile_pics' means the uploaded image will be stored in MEDIA_DIR/profile_pics

    def __str__(self):
        return self.user.username


