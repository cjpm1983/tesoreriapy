from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class UserProfileManager(BaseUserManager):
    def create_user(self,username,password, **extra_fields):
        if not username:
            raise ValueError(_("Te username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Super usermust have is_staff true'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Super user must have is_superuser true'))
