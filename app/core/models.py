from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


#provides helper function for creating users or superusers
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields): #**extra_fields=take any additional field and add them to user model's field on the fly
        """creates and saves new user"""
        if not email:
            raise ValueError("User must have email address!")
        user = self.model(email=self.normalize_email(email), **extra_fields) #nomalize makes everything after @ a lower case => Jweb@Gmail == Jweb@gmail
        user.set_password(password) #method set_password ==> set password for user model
        user.save(using=self._db) #to support multiple db, good practice, though its not used

        return user
    
    def create_superuser(self, email, password):
        """creates and saves new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True #built in method to check if user is admin(superuser)
        user.save(using=self._db)

        return user


#extend from UserManager ==> we can customize this to support our email
#doing this we'll overwrite User object of django
class User(AbstractBaseUser, PermissionsMixin): 
    """Custom user model that extend from UserManager so we can use email instead of username for logging in"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #objects is attribute of models(UserManager)
    #so when we call user.objects.somemethod, we actually call UserManager
    #but with extended user, we only need email and name
    objects = UserManager()

    USERNAME_FIELD = 'email' #very important bit, django magic function, allowing us to use email instead of username


