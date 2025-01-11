from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import django.contrib.auth.hashers as hashers
from django.core.exceptions import ObjectDoesNotExist

class UserEntityManager(BaseUserManager):
    def create_user(self, username, email, password, first_name, last_name):
        if not username:
            raise ValueError("The 'username' field must be set")
        if not email:
            raise ValueError("The 'email' field must be set")
        if not password:
            raise ValueError("The 'password' field must be set")
        if not first_name:
            raise ValueError("The 'first_name' field must be set")
        if not last_name:
            raise ValueError("The 'last_name' field must be set")
        
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name)
        user.is_superuser = False
        user.is_staff = False
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, first_name, last_name):
        user = self.model(email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_admin = True
        
        user.save(using=self._db)
        return user
    
    def authenticate(self, **credentials):
        username = credentials.get('username', None)
        email = credentials.get('email', None)
        password = credentials.get('password', None)

        if not (username or email) or not password:
            return None
        
        user = None
        try:
            if username:
                user = self.get(username=username)
            elif email:
                user = self.get(email=email)
        except self.model.DoesNotExist:
            raise ObjectDoesNotExist
        
        if user and hashers.check_password(password, user.password):
            return user
        
        return None

class UserEntity(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    username = models.CharField(max_length = 30, primary_key=True, unique=True)
    email = models.CharField(max_length = 320, unique=True)
    password = models.CharField(max_length = 256)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    refresh_token = models.CharField(max_length = 20, blank=False)

    objects = UserEntityManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password', 'first_name', 'last_name']

class VibeEntity(models.Model):
    class Meta:
        db_table = 'vibes'
        ordering = ['name']

    COLORS = {
        '#ff0000': 'red',
        '#008000': 'green',
        '#468499': 'blue',
    }
    
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, choices=COLORS)
    danceability = models.FloatField()
    energy = models.FloatField()
    valence = models.FloatField()
    user = models.ForeignKey(UserEntity, on_delete=models.CASCADE)