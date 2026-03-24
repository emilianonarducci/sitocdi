from django.http import JsonResponse
from django.db.models import Q
from .models import Struttura, Fondo, Prestazione
from .search import search_prestazioni


def _struttura_to_dict(s, full=False):
    d = {
        "id": s.id,
        "nome": s.nome,
        "tipo": s.tipo,
        "indirizzo": s.indirizzo,
        "cap": s.cap,
        "citta": s.citta,
        "provincia": s.provincia,
        "telefono": s.telefono,
        "email": s.email,
        "lat": s.lat,
        "lng": s.lng,
        "foto_url": s.foto_url,
        "orari": s.orari,
    }
    if full:
        d["descrizione"] = s.descrizione
        d["servizi"] = [r.strip() for r in s.servizi.splitlines() if r.strip()]
    return d


def search_api(request):
    query = request.GET.get("q", "").strip()
    struttura = request.GET.get("struttura", None)
    fondo = request.GET.get("fondo", None)

    if not query:
        return JsonResponse({"count": 0, "results": []})

    try:
        results = search_prestazioni(query, struttura=struttura, fondo=fondo)
        return JsonResponse({"count": len(results), "results": results})
    except Exception:
        # Fallback su PostgreSQL se OpenSearch non è disponibile
        # Cerca ogni parola con AND: tutte devono essere presenti in nome o descrizione
        from functools import reduce
        import operator as op
        words = query.split()
        word_filters = [
            Q(nome__icontains=w) | Q(descrizione__icontains=w)
            for w in words
        ]
        qs = Prestazione.objects.filter(attiva=True).filter(
            reduce(op.and_, word_filters)
        ).prefetch_related("strutture", "medici", "fondi")[:10]
        results = [
            {
                "id": p.id,
                "nome": p.nome,
                "codice": p.codice,
                "branca": p.get_branca_display(),
                "prezzo_solvente": float(p.prezzo_solvente) if p.prezzo_solvente else None,
                "strutture": [s.nome for s in p.strutture.all()],
                "medici": [m.nome_completo for m in p.medici.all()],
                "fondi": [f.nome for f in p.fondi.all()],
            }
            for p in qs
        ]
        return JsonResponse({"count": len(results), "results": results})


def suggestions_api(request):
    query = request.GET.get("q", "").strip()
    if len(query) < 2:
        return JsonResponse({"suggestions": []})

    qs = Prestazione.objects.filter(
        attiva=True,
        nome__icontains=query
    ).values_list("nome", flat=True)[:8]

    return JsonResponse({"suggestions": list(qs)})


def prestazione_detail_api(request, pk):
    try:
        p = Prestazione.objects.prefetch_related("strutture", "medici__scheda_cms", "fondi").get(pk=pk, attiva=True)
        return JsonResponse({
            "id": p.id,
            "nome": p.nome,
            "codice": p.codice,
            "branca": p.get_branca_display(),
            "descrizione": p.descrizione,
            "prezzo_solvente": float(p.prezzo_solvente) if p.prezzo_solvente else None,
            "strutture": [{"id": s.id, "nome": s.nome, "citta": s.citta, "indirizzo": s.indirizzo, "telefono": s.telefono} for s in p.strutture.all()],
            "medici": [{"nome": m.nome_completo, "specializzazione": m.specializzazione, "scheda_cms_id": m.scheda_cms.id if hasattr(m, "scheda_cms") else None} for m in p.medici.all()],
            "fondi": [{"nome": f.nome, "codice": f.codice} for f in p.fondi.all()],
        })
    except Prestazione.DoesNotExist:
        return JsonResponse({"error": "Non trovata"}, status=404)


def strutture_api(request):
    strutture = Struttura.objects.filter(attiva=True)
    return JsonResponse({"results": [_struttura_to_dict(s) for s in strutture]})


def struttura_detail_api(request, pk):
    try:
        s = Struttura.objects.get(pk=pk, attiva=True)
        return JsonResponse(_struttura_to_dict(s, full=True))
    except Struttura.DoesNotExist:
        return JsonResponse({"error": "Non trovata"}, status=404)


def fondi_api(request):
    fondi = Fondo.objects.all().values("id", "nome", "codice")
    return JsonResponse({"results": list(fondi)})
