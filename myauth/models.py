from django.db import models
from django.contrib.auth.models import User,Group


class SiteUser(User):

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(SiteUser,self).save(*args,**kwargs)
        self.groups.add(Group.objects.get(name="siteuser"))

    def __str__(self):
        return "{}".format(self.get_full_name())
