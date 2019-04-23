from django.db import models
from django.contrib.auth.models import User as LocalUser
from wsocial_site import settings

class User(models.Model):
    nick = models.CharField(max_length=30, null=False, unique=True)
    url = models.URLField(max_length=256, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    local_user = models.ForeignKey(LocalUser, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=True, blank=True)
    remote = models.BooleanField(null=False, default=False)

    following = models.ManyToManyField('User', symmetrical=False, null=True, blank=True)
    def __str__(self):
        return self.name or self.nick

    def get_absolute_url(self):
        return settings.BASE_URL + 'user/%d/' % self.id

    def get_followees(self):
        return self.following.all()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return str(self.user) + "'s Profile"

class Status(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    url = models.URLField(max_length=256, null=True, blank=True)
    text = models.TextField()
    re_status = models.ForeignKey('Status', related_name='re', null=True, blank=True, on_delete=models.SET_NULL)
    shares_status = models.ForeignKey('Status', related_name='shares', null=True, blank=True, on_delete=models.SET_NULL)
    pub_date = models.DateTimeField(null=False)
    remote = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.user.nick + ': ' + self.text

    class Meta:
        ordering = ['-pub_date']

    def get_absolute_url(self):
        return settings.BASE_URL + 'user/%d/status/%d/' % (self.user.id, self.id)
