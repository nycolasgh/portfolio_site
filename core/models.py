from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class About(models.Model):
    short_description = models.TextField(null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About Me"


# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="About Service", null=True)

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    description = models.CharField(max_length=400, verbose_name="Work Description")
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField('Service', blank=True, related_name='Services')
    image = models.ImageField(upload_to="works")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Client Model
class Client(models.Model):
    clientuser = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)  # COMO SALVAR O NOME DO USUARIO LOGADO?
    clientname = models.CharField(max_length=100, blank=True, null=True, verbose_name="Client name")
    companyname = models.CharField(max_length=100, verbose_name="Company name", null=True)
    description = models.TextField(verbose_name="Company Description")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.companyname


class Feedbacks(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    clientname = models.CharField(max_length=100, null=True, verbose_name="Username")
    companyname = models.CharField(max_length=100, verbose_name="Company name", null=True)
    feedback = models.TextField(verbose_name="Feedback")

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

    def __str__(self):
        return self.clientname
