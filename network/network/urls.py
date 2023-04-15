from django.contrib import admin
from django.urls import path, include

from messenger import views
from django.conf.urls.static import static

from network import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about")
]

# handler404 = "messenger.views.page_not_found_view"
# handler403 = "messenger.views.page_forbidden"
# handler400 = "messenger.views.page_bad_request"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
