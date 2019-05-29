from django.conf import settings
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

User = settings.AUTH_USER_MODEL
class ObjectViewed(models.Model):
    user            = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # User instance instance.id
    #ip_address
    content_type    = models.ForeignKey(ContentType) # Product, Order, Cart, Address
    object_id       = models.PositiveIntegerField() # User id, Product id, Order id
    content_object  = GenericForeignKey('content_type', 'object_id') # Product instance
