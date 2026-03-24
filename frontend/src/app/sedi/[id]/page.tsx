import { notFound } from "next/navigation";
import { getSedeDetail } from "@/lib/api";
import SedeMap from "./SedeMap";
import styles from "./page.module.css";

export const revalidate = 300;

const ORARI_LABEL: Record<string, string> = {
  lun_ven: "Lunedì – Venerdì",
  sab: "Sabato",
  dom: "Domenica",
  note: "Note",
};

export default async function SedeDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const sede = await getSedeDetail(Number(id));
  if (!sede) notFound();

  const googleMapsUrl = sede.lat && sede.lng
    ? `https://www.google.com/maps/dir/?api=1&destination=${sede.lat},${sede.lng}`
    : `https://www.google.com/maps/search/${encodeURIComponent(sede.indirizzo + " " + sede.citta)}`;

  return (
    <>
      {/* HERO */}
      <section className={styles.hero}>
        <div className={styles.heroBadge}>LE NOSTRE SEDI</div>
        <h1 className={styles.heroName}>{sede.nome}</h1>
        <p className={styles.heroAddr}>{sede.indirizzo} · {sede.cap} {sede.citta} ({sede.provincia})</p>
        {sede.telefono && (
          <a href={`tel:${sede.telefono}`} className={styles.heroTel}>{sede.telefono}</a>
        )}
      </section>

      <div className={styles.body}>
        <div className={styles.container}>
          <a href="/sedi" className={styles.backBtn}>← Tutte le sedi</a>

          <div className={styles.layout}>
            {/* MAIN */}
            <div className={styles.main}>

              {/* Foto + descrizione */}
              {sede.foto_url && (
                // eslint-disable-next-line @next/next/no-img-element
                <img src={sede.foto_url} alt={sede.nome} className={styles.foto} />
              )}

              {sede.descrizione && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>La sede</h2>
                  <p className={styles.descrizione}>{sede.descrizione}</p>
                </div>
              )}

              {/* Servizi */}
              {sede.servizi?.length > 0 && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>Servizi disponibili</h2>
                  <div className={styles.serviziGrid}>
                    {sede.servizi.map((s) => (
                      <div key={s} className={styles.servizioItem}>
                        <span className={styles.servizioCheck}>✓</span> {s}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Mappa */}
              {sede.lat && sede.lng && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>Come raggiungerci</h2>
                  <SedeMap sede={sede as unknown as import("@/lib/api").Sede} />
                  <a href={googleMapsUrl} target="_blank" rel="noopener noreferrer" className={styles.directionsBtn}>
                    Ottieni indicazioni su Google Maps →
                  </a>
                </div>
              )}
            </div>

            {/* SIDEBAR */}
            <aside className={styles.sidebar}>
              {/* Orari */}
              {Object.keys(sede.orari ?? {}).length > 0 && (
                <div className={styles.infoCard}>
                  <h3 className={styles.infoCardTitle}>Orari</h3>
                  <dl className={styles.orariList}>
                    {Object.entries(sede.orari).map(([k, v]) => (
                      <div key={k} className={styles.orarioRow}>
                        <dt className={styles.orarioGiorno}>{ORARI_LABEL[k] ?? k}</dt>
                        <dd className={`${styles.orarioValore} ${v === "Chiuso" ? styles.chiuso : ""}`}>{v}</dd>
                      </div>
                    ))}
                  </dl>
                </div>
              )}

              {/* Contatti */}
              <div className={styles.infoCard}>
                <h3 className={styles.infoCardTitle}>Contatti</h3>
                <div className={styles.contattiList}>
                  <div className={styles.contattoRow}>
                    <span>📍</span>
                    <span>{sede.indirizzo}, {sede.cap} {sede.citta}</span>
                  </div>
                  {sede.telefono && (
                    <div className={styles.contattoRow}>
                      <span>📞</span>
                      <a href={`tel:${sede.telefono}`} className={styles.contattoLink}>{sede.telefono}</a>
                    </div>
                  )}
                  {sede.email && (
                    <div className={styles.contattoRow}>
                      <span>✉️</span>
                      <a href={`mailto:${sede.email}`} className={styles.contattoLink}>{sede.email}</a>
                    </div>
                  )}
                </div>
              </div>

              {/* CTA */}
              <div className={styles.ctaCard}>
                <p className={styles.ctaText}>Prenota in questa sede</p>
                <a href="/cerca" className={styles.ctaBtn}>PRENOTA ORA</a>
              </div>
            </aside>
          </div>
        </div>
      </div>
    </>
  );
}
