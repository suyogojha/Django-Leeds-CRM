


from django.contrib import admin
from django.urls import path, include
from leads.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('', landing_page, name='landing-page' ),
    # class based view url 
    # path('', LandingpageView.as_view(), name='landing-page' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)