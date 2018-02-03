from django.db import models
from django.core.mail import send_mail
# from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator
import datetime

class MyUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		'''
		creates and saves a User with the give email and password
		'''
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(email = self.normalize_email(email))
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		'''
		creates and saves a superuser with the given email and password
		'''
		user = self.create_user(email, password=password)
		user.is_admin = True
		user.save(using=self._db)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(_('email address'), max_length=255, unique=True)
	first_name = models.CharField(_('first name'), max_length=30, null = True)
	last_name = models.CharField(_('last name'), max_length=30, null = True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	def get_full_name(self):
		'''
		returns the first and last name of the user
		'''
		full_name = '%s %s' %(self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		'''
		returns the first name of the user
		'''
		return self.first_name

	def __str__(self):

		return ('%s  %s' %(self.first_name, self.email)) 

	def has_perm(self, perm, obj=None):
		'''
		Returns True if the user has the specified permission, 
		where perm is in the format "<app label>.<permission codename>".
		'''
		return True

	def has_module_perms(self, app_label):
		'''
		Returns True if the user has any permissions in the given package
		(the Django app label). If the user is inactive, this method will 
		 always return False
		'''
		return True

	@property
	def is_staff(self):

		return self.is_admin











