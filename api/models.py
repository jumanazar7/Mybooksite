from django.db import models
from accounts.models import Customuser
from .managers import PublishedManager
from django.utils.text import  slugify

class Post(models.Model):
    STATUS = {
        ('draft','Draft'),
        ('publish','Publish'),

        
    }
    author = models.ForeignKey(Customuser,on_delete=models.CASCADE)
    title  = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="posts/%Y/%m/%d")
    status = models.CharField(max_length=15,choices=STATUS,default='draft')
    objects = models.Manager()
    published = PublishedManager()

    def save(self,*args,**kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    def __str__(self) -> str:
        return self.title