from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin


# class UserAccountManager(BaseUserManager):
#   def create_user(self, phone,role, username, email, password=None):
#     if not email:
#       raise ValueError('Users must have an email address')

#     email = self.normalize_email(email)
#     email = email.lower()

#     user = self.model(
#       username=username,
#       role=role,
#       phone=phone,
#       email=email,
#     )

#     user.set_password(password)
#     user.save(using=self._db)

#     return user
  

  
  # def create_superuser(self, email, password=None):
  #   user = self.create_user(
  #     email,
  #     password=password,
  #   )

  #   user.is_staff = True
  #   user.is_superuser = True
  #   user.save(using=self._db)

  #   return user


class UserAccount(AbstractUser):
  ROLES = (
      ('admin', 'Admin'),
      ('customer', 'Customer')
  )
  ALLOWED_COUNTRIES = (
      ('japan','Japan'),
      ('france','France'),
      ('germany','Germany'),
      ('china','China')
  )
  email = models.EmailField(null=True, unique=True)
  phone = models.CharField(max_length=10, null=True , unique=True)
  username = models.CharField(max_length=50, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  role = models.CharField(choices=ROLES, max_length=10)
  country = models.CharField(choices=ALLOWED_COUNTRIES, max_length=10, default="")


  # objects = UserAccountManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  # def __str__(self):
  #   return self.email
