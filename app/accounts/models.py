from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import validate_email
from django.db import models


class UserManager(BaseUserManager):

    def create(self, name, email, password, is_active=False):
        validate_email(email)
        user = self.model(
            name=name,
            email=self.normalize_email(email),
            is_active=is_active,
        )
        user.set_password(password)
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
    ]
    name = models.CharField(max_length=160)
    email = models.EmailField(max_length=160, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'
        ordering = ['name']
