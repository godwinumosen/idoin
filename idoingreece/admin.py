from django.contrib import admin
from .models import (
    IdoingreecePost,
    ExceptionalIdoingreecePost,
    Feature2_IdoingreecePost,
    SecondIdoingreecePost,
    AboutIdoingreecePost,
    FirstIdoingreecePost,
    ExcellenceIdoingreecePost,
    NotifyNewsIdoingreecePost,
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


class ExceptionalIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Exceptional_Idoingreece_slug': ('Exceptional_Idoingreece_title',)}
    list_display = ['Exceptional_Idoingreece_title', 'Exceptional_Idoingreece_description', 'Exceptional_Idoingreece_author']

admin.site.register(ExceptionalIdoingreecePost, ExceptionalIdoingreecePostModelAdmin)


class Feature2_IdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Feature2_Idoingreece_slug': ('Feature2_Idoingreece_title',)}
    list_display = ['Feature2_Idoingreece_title', 'Feature2_Idoingreece_description', 'Feature2_Idoingreece_author']

admin.site.register(Feature2_IdoingreecePost, Feature2_IdoingreecePostModelAdmin)


class FirstIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'First_Idoingreece_slug': ('First_Idoingreece_title',)}
    list_display = ['First_Idoingreece_title', 'First_Idoingreece_description', 'First_Idoingreece_author']

admin.site.register(FirstIdoingreecePost, FirstIdoingreecePostModelAdmin)


class ExcellenceIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Excellence_Idoingreece_slug': ('Excellence_Idoingreece_title',)}
    list_display = ['Excellence_Idoingreece_title', 'Excellence_Idoingreece_description', 'Excellence_Idoingreece_author']

admin.site.register(ExcellenceIdoingreecePost, ExcellenceIdoingreecePostModelAdmin)


class SecondIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'Second_Idoingreece_slug': ('Second_Idoingreece_title',)}
    list_display = ['Second_Idoingreece_title', 'Second_Idoingreece_description', 'Second_Idoingreece_author']

admin.site.register(SecondIdoingreecePost, SecondIdoingreecePostModelAdmin)


class NotifyNewsIdoingreecePostModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'NotifyNews_Idoingreece_slug': ('NotifyNews_Idoingreece_title',)}
    list_display = ['NotifyNews_Idoingreece_title', 'NotifyNews_Idoingreece_description', 'NotifyNews_Idoingreece_author']

admin.site.register(NotifyNewsIdoingreecePost, NotifyNewsIdoingreecePostModelAdmin)