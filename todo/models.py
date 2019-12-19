from django.db import models
# Create your models here.

# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title


class SignUp(models.Model):
  uname = models.CharField(max_length=120)
  apt = models.CharField(max_length=4)
  email = models.CharField(max_length=60)
  pwd = models.CharField(max_length=60)

