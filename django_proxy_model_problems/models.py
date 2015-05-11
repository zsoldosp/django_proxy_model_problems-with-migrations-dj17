from django.contrib.auth.models import User


class MyProxyUser(User):
    class Meta:
        proxy = True

