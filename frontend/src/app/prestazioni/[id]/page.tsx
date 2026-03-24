"use client";
import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { getPrestazioneDetail, type PrestazioneDetail } from "@/lib/api";
import styles from "./page.module.css";

export default function PrestazioneDetailPage() {
  const { id } = useParams<{ id: string }>();
  const router = useRouter();
  const [prestazione, setPrestazione] = useState<PrestazioneDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPrestazioneDetail(Number(id))
      .then(setPrestazione)
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) return <div className={styles.loading}>Caricamento...</div>;
  if (!prestazione) return <div className={styles.loading}>Prestazione non trovata.</div>;

  return (
    <div className={styles.page}>
      <div className="container">
        <button className={styles.backBtn} onClick={() => router.back()}>← Torna ai risultati</button>

        <div className={styles.layout}>
          {/* Colonna principale */}
          <div className={styles.main}>
            <div className={styles.hero}>
              <span className={styles.branca}>{prestazione.branca}</span>
              {prestazione.codice && <span className={styles.codice}>Cod. {prestazione.codice}</span>}
              <h1>{prestazione.nome}</h1>
              {prestazione.descrizione && <p className={styles.desc}>{prestazione.descrizione}</p>}
            </div>

            {/* Medici */}
            {prestazione.medici.length > 0 && (
              <div className={styles.section}>
                <h2>Medici che erogano la prestazione</h2>
                <div className={styles.medicoGrid}>
                  {prestazione.medici.map((m) => (
                    <div key={m.nome} className={styles.medicoCard}>
                      <div className={styles.medicoAvatar}>
                        {m.nome.charAt(m.nome.indexOf(" ") + 1) || m.nome.charAt(0)}
                      </div>
                      <div>
                        <div className={styles.medicoNome}>{m.nome}</div>
                        <div className={styles.medicoSpec}>{m.specializzazione}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Sedi */}
            {prestazione.strutture.length > 0 && (
              <div className={styles.section}>
                <h2>Sedi disponibili</h2>
                <div className={styles.sediGrid}>
                  {prestazione.strutture.map((s) => (
                    <div key={s.id} className={styles.sedeCard}>
                      <div className={styles.sedeNome}>{s.nome}</div>
                      <div className={styles.sedeInfo}>📍 {s.indirizzo}, {s.citta}</div>
                      {s.telefono && <div className={styles.sedeInfo}>📞 {s.telefono}</div>}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Sidebar */}
          <div className={styles.sidebar}>
            <div className={styles.priceCard}>
              <div className={styles.priceLabel}>Prezzo solvente</div>
              {prestazione.prezzo_solvente ? (
                <div className={styles.priceValue}>€ {prestazione.prezzo_solvente}</div>
              ) : (
                <div className={styles.priceNA}>Su richiesta</div>
              )}
              <button className={styles.prenotaBtn}>Prenota ora</button>
              <p className={styles.prenotaNote}>Seleziona sede e data dopo aver cliccato</p>
            </div>

            {prestazione.fondi.length > 0 && (
              <div className={styles.fondiCard}>
                <h3>Fondi che coprono questa prestazione</h3>
                <ul>
                  {prestazione.fondi.map((f) => (
                    <li key={f.nome}>
                      <span className={styles.fondoCheck}>✓</span> {f.nome}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
