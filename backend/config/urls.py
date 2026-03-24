from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from prestazioni.views import search_api, strutture_api, fondi_api, suggestions_api, prestazione_detail_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/prestazioni/search/", search_api, name="prestazioni-search"),
    path("api/strutture/", strutture_api, name="strutture"),
    path("api/fondi/", fondi_api, name="fondi"),
    path("api/prestazioni/suggestions/", suggestions_api, name="suggestions"),
    path("api/prestazioni/<int:pk>/", prestazione_detail_api, name="prestazione-detail"),
    path("api/cms/", include("contenuto.urls")),
    path("", include("cms.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
