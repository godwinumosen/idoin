from django.contrib import admin
from .models import (
    IdoingreecePost,
    Feature2_IdoingreecePost,
    SecondIdoingreecePost,
    AboutIdoingreecePost,
    FirstIdoingreecePost,
    ExcellenceIdoingreecePost,
    NotifyNewsIdoingreecePost,
    ContactMessage,
)

# Main post
class IdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Idoingreece_slug': ('Idoingreece_title',)}
    list_display = ['Idoingreece_title', 'Idoingreece_description', 'Idoingreece_author']

admin.site.register(IdoingreecePost, IdoingreecePostModelAdmin)


class AboutIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'About_Idoingreece_slug': ('About_Idoingreece_title',)}
    list_display = ['About_Idoingreece_title', 'About_Idoingreece_description', 'About_Idoingreece_author']

admin.site.register(AboutIdoingreecePost, AboutIdoingreecePostModelAdmin)



class ContactMessageModelAdmin (admin.ModelAdmin):
    list_display = ['name','subject','email','created_at']
admin.site.register(ContactMessage, ContactMessageModelAdmin)

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'category')
    list_filter = ('publish_date', 'category')
    search_fields = ('title', 'author', 'content')
    date_hierarchy = 'publish_date'



class FirstIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'First_Idoingreece_slug': ('First_Idoingreece_title',)}
    list_display = ['First_Idoingreece_title', 'First_Idoingreece_description', 'First_Idoingreece_author']

admin.site.register(FirstIdoingreecePost, FirstIdoingreecePostModelAdmin)


class Feature2_IdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Feature2_Idoingreece_slug': ('Feature2_Idoingreece_title',)}
    list_display = ['Feature2_Idoingreece_title', 'Feature2_Idoingreece_description', 'Feature2_Idoingreece_author']

admin.site.register(Feature2_IdoingreecePost, Feature2_IdoingreecePostModelAdmin)




class SecondIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Second_Idoingreece_slug': ('Second_Idoingreece_title',)}
    list_display = ['Second_Idoingreece_title', 'Second_Idoingreece_description', 'Second_Idoingreece_author']

admin.site.register(SecondIdoingreecePost, SecondIdoingreecePostModelAdmin)


class NotifyNewsIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'NotifyNews_Idoingreece_slug': ('NotifyNews_Idoingreece_title',)}
    list_display = ['NotifyNews_Idoingreece_title', 'NotifyNews_Idoingreece_description', 'NotifyNews_Idoingreece_author']

admin.site.register(NotifyNewsIdoingreecePost, NotifyNewsIdoingreecePostModelAdmin)


