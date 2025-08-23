from django.db import models
from datetime import date
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    body = models.TextField()
    picture = models.ImageField(upload_to="blog/posts/%y/%m")
    author = models.ForeignKey('accounts.CustomUser' , on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    slug = models.SlugField(default=title,unique=True,blank=True)
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    