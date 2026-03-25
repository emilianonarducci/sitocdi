from django.urls import path
from . import views

urlpatterns = [
    path("hero/", views.hero_api),
    path("consigliati/", views.consigliati_api),
    path("perche-sceglierci/", views.perche_sceglierci_api),
    path("salute-per-te/", views.salute_per_te_api),
    path("medici/", views.medici_list_api),
    path("medici/<int:pk>/", views.medico_detail_api),
    path("newsletter/subscribe/", views.newsletter_subscribe, name="newsletter_subscribe"),
    path("upload-cv/", views.upload_cv_pdf, name="upload_cv_pdf"),
    path("upload-cv/status/<int:job_id>/", views.cv_import_status, name="cv_import_status"),
]
