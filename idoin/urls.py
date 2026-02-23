from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', include('members.urls')),
    #path('members/', include(('members.urls', 'members'), namespace='members')),

    path('', include('idoingreece.urls')),
]

# Custom Admin Titles
admin.site.site_header = "idoingreece Admin"
admin.site.site_title = "idoingreece"

# Serve media and static in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
