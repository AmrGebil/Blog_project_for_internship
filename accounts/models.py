
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise  ValueError('user must have email address')
        if not username:
            raise  ValueError('user must have username')
        user =self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,

        )
        user.is_admin=True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True

        user.save(using=self._db)
        return user



class Account(AbstractBaseUser,PermissionsMixin):
    username= models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)

    #required
    data_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects=MyAccountManager()


    def get_all_permissions(self, obj=None):
        if not self.is_active:
            return set()

        if obj is not None and self.is_anonymous:
            return set()

        if obj is not None:
            # Ensure that self.get_group_permissions(obj) returns a queryset
            return self.user_permissions.all() | self.get_group_permissions(obj).all()

        return self.user_permissions.all() | self.get_group_permissions(obj)

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True





class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='accounts/profile', blank=True)
    bio = models.CharField(max_length=200, blank=True)
    frist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user.email

