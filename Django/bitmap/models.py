from django.db import models

class PicGallery(models.Model):
    id = models.IntegerField(primary_key = True)
    imgpath = models.TextField(null=False, blank = False)
    title = models.TextField(null = False, blank = False)

    def __str__(self):
        return f'{self.id} {self.title} {self.imgpath}'

class UserFeedback(models.Model):
    id = models.AutoField(primary_key = True)
    userfb = models.TextField(null = False, blank = False)
    email = models.EmailField(null = False, blank = False)
    subject = models.TextField(null  = False, blank = False)

    def __str__(self):
        return f'{self.subject}   {self.email}   {self.userfb}'
