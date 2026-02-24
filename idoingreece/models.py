from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class IdoingreecePost(models.Model):
    Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    Idoingreece_description = models.TextField()
    Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    Idoingreece_img = models.ImageField(upload_to='idoingreece_images/')
    Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-Idoingreece_publish_date']

    def __str__(self):
        return f"{self.Idoingreece_title} | {self.Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    


class AboutIdoingreecePost(models.Model):
    About_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    About_Idoingreece_description = models.TextField()
    About_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    About_Idoingreece_img = models.ImageField(upload_to='About_images/')
    About_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    About_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-About_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.About_Idoingreece_title} | {self.About_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    


class ExceptionalIdoingreecePost(models.Model):
    Exceptional_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    Exceptional_Idoingreece_status = models.CharField(max_length=255, blank=True, null=True)
    Exceptional_Idoingreece_description = models.TextField()
    Exceptional_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    Exceptional_Idoingreece_img = models.ImageField(upload_to='Exceptional_images/')
    Exceptional_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    Exceptional_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-Exceptional_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.Exceptional_Idoingreece_title} | {self.Exceptional_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    

class Feature2_IdoingreecePost(models.Model): 
    Feature2_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    Feature2_Idoingreece_status = models.CharField(max_length=255, blank=True, null=True)
    Feature2_Idoingreece_description = models.TextField()
    Feature2_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    Feature2_Idoingreece_img = models.ImageField(upload_to='Feature2_images/')
    Feature2_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    Feature2_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-Feature2_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.Feature2_Idoingreece_title} | {self.Feature2_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    


class FirstIdoingreecePost(models.Model):
    First_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    First_Idoingreece_description = models.TextField()
    First_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    First_Idoingreece_img = models.ImageField(upload_to=' First_images/')
    First_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    First_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-First_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.First_Idoingreece_title} | {self.First_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    



class ExcellenceIdoingreecePost(models.Model): 
    Excellence_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    Excellence_Idoingreece_description = models.TextField()
    Excellence_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    Excellence_Idoingreece_img = models.ImageField(upload_to='Excellence_images/')
    Excellence_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    Excellence_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-Excellence_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.Excellence_Idoingreece_title} | {self.Excellence_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    



class SecondIdoingreecePost(models.Model):
    Second_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    Second_Idoingreece_description = models.TextField()
    Second_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    Second_Idoingreece_img = models.ImageField(upload_to='Second_idoingreece_images/')
    Second_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    Second_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-Second_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.Second_Idoingreece_title} | {self.Second_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')
    
class NotifyNewsIdoingreecePost(models.Model):   
    NotifyNews_Idoingreece_title = models.CharField(max_length=255, blank=True, null=True)
    NotifyNews_Idoingreece_description = models.TextField()
    NotifyNews_Idoingreece_slug = models.SlugField(max_length=255, blank=True, null=True)
    NotifyNews_Idoingreece_img = models.ImageField(upload_to='NotifyNews_images/')
    NotifyNews_Idoingreece_publish_date = models.DateTimeField(auto_now_add=True)
    NotifyNews_Idoingreece_author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-NotifyNews_Idoingreece_publish_date']

    def __str__(self):
        return f"{self.NotifyNews_Idoingreece_title} | {self.NotifyNews_Idoingreece_author}"

    def get_absolute_url(self):
        return reverse('home')