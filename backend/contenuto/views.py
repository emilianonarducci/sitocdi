from django.http import JsonResponse
from .models import HeroSlide, ConsigliatiCard, PercheSceglierciSezione, SalutePerTeArticolo, SchedaMedico


def hero_api(request):
    slides = HeroSlide.objects.filter(attivo=True)
    return JsonResponse([{
        "id": s.id,
        "badge": s.badge,
        "titolo": s.titolo,
        "sottotitolo": s.sottotitolo,
        "cta_testo": s.cta_testo,
        "cta_link": s.cta_link,
        "immagine_url": s.immagine_url,
    } for s in slides], safe=False)


def consigliati_api(request):
    cards = ConsigliatiCard.objects.filter(attivo=True)
    return JsonResponse([{
        "id": c.id,
        "titolo": c.titolo,
        "immagine_url": c.immagine_url,
        "link": c.link,
    } for c in cards], safe=False)


def perche_sceglierci_api(request):
    try:
        sezione = PercheSceglierciSezione.objects.first()
        if not sezione:
            return JsonResponse({}, safe=False)
        return JsonResponse({
            "titolo": sezione.titolo,
            "descrizione": sezione.descrizione,
            "immagine_sfondo_url": sezione.immagine_sfondo_url,
            "cards": [{
                "id": c.id,
                "variante": c.variante,
                "titolo": c.titolo,
                "descrizione": c.descrizione,
            } for c in sezione.cards.all()],
        })
    except Exception:
        return JsonResponse({}, safe=False)


def salute_per_te_api(request):
    tab = request.GET.get("tab")
    qs = SalutePerTeArticolo.objects.filter(attivo=True)
    if tab:
        qs = qs.filter(tab=tab)
    return JsonResponse([{
        "id": a.id,
        "tab": a.tab,
        "titolo": a.titolo,
        "descrizione": a.descrizione,
        "immagine_url": a.immagine_url,
        "link": a.link,
    } for a in qs], safe=False)


def _medico_to_dict(m: SchedaMedico) -> dict:
    return {
        "id": m.id,
        "nome_completo": m.nome_completo,
        "specializzazione": m.specializzazione,
        "ruolo": m.ruolo,
        "foto_url": m.foto_url,
        "bio": m.bio,
        "titoli_accademici": m.titoli_accademici,
        "esperienze_professionali": m.esperienze_professionali,
        "pubblicazioni": m.pubblicazioni,
        "link_prenota": m.link_prenota,
    }


def medici_list_api(request):
    qs = SchedaMedico.objects.filter(attivo=True)
    return JsonResponse([_medico_to_dict(m) for m in qs], safe=False)


def medico_detail_api(request, pk: int):
    try:
        m = SchedaMedico.objects.get(pk=pk, attivo=True)
        return JsonResponse(_medico_to_dict(m))
    except SchedaMedico.DoesNotExist:
        return JsonResponse({"error": "Non trovato"}, status=404)
