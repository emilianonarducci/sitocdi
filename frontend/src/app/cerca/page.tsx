"use client";
import { useEffect, useState } from "react";
import { useSearchParams, useRouter } from "next/navigation";
import { searchPrestazioni, type Prestazione } from "@/lib/api";
import styles from "./page.module.css";

export default function CercaPage() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const q = searchParams.get("q") || "";
  const struttura = searchParams.get("struttura") || "";

  const [results, setResults] = useState<Prestazione[]>([]);
  const [count, setCount] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!q) return;
    setLoading(true);
    searchPrestazioni(q, struttura || undefined)
      .then((data) => {
        setResults(data.results);
        setCount(data.count);
      })
      .finally(() => setLoading(false));
  }, [q, struttura]);

  return (
    <div className={styles.page}>
      <div className="container">
        <div className={styles.header}>
          <button className={styles.backBtn} onClick={() => router.back()}>← Torna indietro</button>
          <h1>Risultati per <span>&quot;{q}&quot;</span></h1>
          {struttura && <p className={styles.filterLabel}>Sede: {struttura}</p>}
        </div>

        {loading && <div className={styles.loading}>Ricerca in corso...</div>}

        {!loading && count === 0 && (
          <div className={styles.empty}>
            <p>Nessuna prestazione trovata per &quot;{q}&quot;.</p>
            <p>Prova con un termine diverso oppure <a href="/">torna alla home</a>.</p>
          </div>
        )}

        {!loading && count > 0 && (
          <>
            <p className={styles.countLabel}>{count} prestazioni trovate</p>
            <div className={styles.grid}>
              {results.map((r) => (
                <div
                  key={r.id}
                  className={styles.card}
                  onClick={() => router.push(`/prestazioni/${r.id}`)}
                >
                  <div className={styles.cardTop}>
                    <span className={styles.branca}>{r.branca}</span>
                    {r.prezzo_solvente && (
                      <span className={styles.prezzo}>€ {r.prezzo_solvente}</span>
                    )}
                  </div>
                  <h3>{r.nome}</h3>
                  {r.descrizione && <p className={styles.desc}>{r.descrizione}</p>}
                  <div className={styles.cardMeta}>
                    {r.strutture?.length > 0 && (
                      <span className={styles.sedi}>📍 {r.strutture.length} {r.strutture.length === 1 ? "sede" : "sedi"}</span>
                    )}
                    {r.fondi?.length > 0 && (
                      <span className={styles.fondi}>✓ Fondi disponibili</span>
                    )}
                  </div>
                  <button className={styles.detailBtn}>Vedi dettaglio →</button>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
