from django.conf import settings
from django.db import models # this django modes is use to create a table on database
from django.utils import timezone # time zone helps to identify ur geogrphical time when working on time in inputs


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE) # by convention django AUTH is use when foriegn key is there
    title = models.CharField(max_length = 200) 
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to='media')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    # this method is use to publish 
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # by convention this comes with every model table to return the toString of title in this case
    def __str__(self) :
        return self.title


# Create your models here.
