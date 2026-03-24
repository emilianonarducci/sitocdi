from django.urls import path
from . import views

urlpatterns = [
    path("hero/", views.hero_api),
    path("consigliati/", views.consigliati_api),
    path("perche-sceglierci/", views.perche_sceglierci_api),
    path("salute-per-te/", views.salute_per_te_api),
    path("medici/", views.medici_list_api),
    path("medici/<int:pk>/", views.medico_detail_api),
]
