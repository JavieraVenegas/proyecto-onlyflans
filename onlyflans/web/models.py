from email import message
from email.policy import default
import uuid
import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length=64)
    descrption = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()


class Personalizado(models.Model):
    personalizado_uuid = models.UUIDField()
    name_especial = models.CharField(max_length=64)
    description_especial = models.TextField()
    image_especial = models.URLField()
    