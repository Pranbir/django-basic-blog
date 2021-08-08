from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class category(models.Model):
    pass

class blogpost(models.Model):
    title= models.CharField(default="N/A", null=False, max_length=50)
    content = tinymce_models.HTMLField()
    blog_img =  models.ImageField(null=True, upload_to='upload', max_length=None)

    def __str__(self):
        return self.title


class comments(models.Model):
    comment_data = models.TextField(null=False)
    parent_post = models.ForeignKey(blogpost, on_delete=models.CASCADE)

class temptable(models.Model):
    browser_data = models.TextField(null=True)