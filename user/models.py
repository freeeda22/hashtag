from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,username, password, email=None, phone=None, is_staff=False, is_admin=False, is_active=True):
        """
        Create and save a User with the given email and password.
        """
        if not password:
            raise ValueError('The Password must be set')
        
        if not(email or phone):
            raise ValueError('The Email or Phone must be set')


        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)  # change user password
        user.username = username
        user.email = email
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user


    def create_superuser(self, username,email, password):

        user = self.create_user(
            username=username,
            email=email,
            password=password,
            phone=None,
            is_staff=True,
            is_admin=True


        )
      
        return user
        
class User(AbstractBaseUser):
    username=models.CharField(null=True,max_length=6,unique=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    bio=models.TextField()
    mobile=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.BooleanField( default=False)
    admin = models.BooleanField( default=False)
    staff = models.BooleanField( default=False)
    active = models.BooleanField( default=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name= 'user'
        verbose_name= 'users'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active
