from django.db import models
from django.utils import timezone

class Post(models.Model):

    post_name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    post_text = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "id": self.id,
            "post_name": self.name,
            "pub_date": str(self.pub_date),
            "post_text": self.post_text,
        }

    class Meta:
        verbose_name = u'Posts'
        verbose_name_plural = u'Posts'

