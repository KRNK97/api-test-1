from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


class CustomManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if email is None:
            raise ValueError("email cant be empty")

        email =  self.normalize_email(email)
        user = self.model(email=email, username=username)                       # create obj of the model with email and username
        user.set_password(password)                                             # set hashed password for it
        user.save(using=self._db)                                               # save the user and specify db to use (optional)

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email,username,password)
        user.is_staff = True
        user.is_superuser = True                                               # is_superuser field is automatically created from the permissions mixin 
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser,PermissionsMixin):

    countries = (
        ('IND','India'),
        ('SRI','Sri Lanka'),
        ('AUS','Australia'),
        ('CHN','China'),
        ('CAN','Canada'),
    )

    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.IntegerField(default=0)
    country = models.CharField(default="IND",choices=countries,max_length=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = CustomManager()