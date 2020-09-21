from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.db import models


class UserManager(BaseUserManager):

	def _create_user(self, username, password, email, **kwargs):
		if not username:
			raise ValueError(u"请输入用户名")
		if not password:
			raise ValueError(u"请输入密码")
		if not email:
			raise ValueError(u"请输入邮箱地址")

		user = self.model(username=username, email=email, **kwargs)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, username, password, email, **kwargs):
		kwargs['is_superuser'] = False
		return self._create_user(username, password, email, **kwargs)

	def create_superuser(self, username, password, email, **kwargs):
		kwargs['is_superuser'] = True
		kwargs['is_staff'] = True
		return self._create_user(username, password, email, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
	GENDER_TYPE = (
		('1', '男'),
		('2', '女'),
	)

	username = models.CharField(max_length=50, verbose_name="用户名", unique=True)
	nickname = models.CharField(max_length=50, verbose_name="昵称", null=True)
	age = models.PositiveSmallIntegerField(verbose_name="年龄", null=True, blank=True)
	gender = models.CharField(max_length=10, choices=GENDER_TYPE, verbose_name="性别", null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="电话号码")
	email = models.EmailField(verbose_name="邮箱")
	picture = models.ImageField(upload_to="profile/%Y/%m/%d", verbose_name="头像", null=True, blank=True)
	home_address = models.CharField(max_length=200, null=True, blank=True, verbose_name="地址")
	is_active = models.BooleanField(default=False, verbose_name="状态")
	is_staff = models.BooleanField(default=True, verbose_name="是否是员工")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

	groups = models.ManyToManyField(
		Group,
		verbose_name=_('groups'),
		blank=True,
		help_text=_(
			'The groups this user belongs to. A user will get all permissions '
			'granted to each of their groups.'
		),
		related_name="user_set",
		related_query_name="user",
	)
	user_permissions = models.ManyToManyField(
		Permission,
		verbose_name=_('user permissions'),
		blank=True,
		help_text=_('Specific permissions for this user.'),
		related_name="user_set",
		related_query_name="user",
	)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']
	EMAIL_FIELD = 'email'

	objects = UserManager()

	def __str__(self):
		return self.username

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.nickname if self.nickname else self.username

	class Meta:
		verbose_name = "用户"
		verbose_name_plural = verbose_name
		db_table = "auth_user"

