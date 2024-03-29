from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from Amisacb.settings import DISABLED

admin.site.site_header = 'Amisa360'
admin.site.site_title = 'Amisa360'

handler400 = 'Amisacb.errors.custom_400'
handler403 = 'Amisacb.errors.custom_403'
handler404 = 'Amisacb.errors.custom_404'
handler500 = 'Amisacb.errors.custom_500'

urlpatterns = []

if not DISABLED:
    STATIC_URL = settings.STATIC_URL.replace('/', '')

    urlpatterns += [
        path('', include('accounts.urls')),
        path('', include('home.urls')),
        path('', include('codes.urls')),
        path('', include('services.urls')),
        path('', include('blog.urls')),
        path('admin/', admin.site.urls)
    ]


    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    def maintenance(request):
        template_name = 'maintenance.html'
        return render(request, template_name)

    urlpatterns += [
        path('', maintenance)
    ]
