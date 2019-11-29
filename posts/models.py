from django.db import models
from django.conf.urls import url
from django.db import models
import os
from uuid import uuid4

import hashlib
import datetime
import os
from functools import partial

def _update_filename(instance, filename, path):
    path = path
    filename = "ff.jpg"
    return os.path.join(path, filename)
def upload_to(path):
    return partial(_update_filename, path=path)

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to=upload_to("images/"))

    def __str__(self):
        return self.title




