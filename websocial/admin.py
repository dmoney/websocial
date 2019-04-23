from django.contrib import admin
from websocial.models import User, Status, Profile

# Register your models here.
for it in [User, Status, Profile]:
    admin.site.register(it)

