from django.db import models
from django.urls import reverse

from django.conf import settings
from django.utils import timezone


#Done
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
    

#Done
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
    

#------------------------------------------------------------------------------------------
#FOR THE VENDOR
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()


class Vendor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,  # FIXED: replaced User
        on_delete=models.CASCADE
    )
    business_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    locations = models.ManyToManyField(Location)

    bio = models.TextField()
    services = models.TextField()
    languages = models.CharField(max_length=255)

    website = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    listing_type = models.CharField(
        choices=[
            ('free', 'Free'),
            ('standard', 'Standard'),
            ('premium', 'Premium'),
        ],
        max_length=20
    )

    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)


class VendorImage(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="vendors/")


class VendorEnquiry(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# ----------------------------
# BLOG MODEL
# ----------------------------

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)  
    blog_image = models.ImageField(upload_to="blog/")

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # FIXED: replaced User
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)


class AdZone(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="ads/")
    link = models.URLField()
    is_active = models.BooleanField(default=True)


#Done
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    