import { notFound } from "next/navigation";
import { getMedico } from "@/lib/cms";
import styles from "./page.module.css";

export const revalidate = false; // on-demand via revalidateTag("cms-medici")

export default async function SchedaMedicoPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = await params;
  const medico = await getMedico(Number(id));

  if (!medico) notFound();

  return (
    <>
      {/* HERO */}
      <section className={styles.hero}>
        <div className={styles.heroBadge}>I NOSTRI MEDICI</div>
        <h1 className={styles.heroName}>{medico.nome_completo}</h1>
        <p className={styles.heroSpec}>{medico.specializzazione}</p>
        {medico.ruolo && <p className={styles.heroRuolo}>{medico.ruolo}</p>}
      </section>

      <div className={styles.body}>
        <div className={styles.container}>
          <div className={styles.layout}>

            {/* COLONNA PRINCIPALE */}
            <div className={styles.main}>

              {/* Bio introduttiva */}
              {medico.bio && (
                <div className={styles.bio}>
                  <p>{medico.bio}</p>
                </div>
              )}

              {/* Titoli Accademici */}
              {medico.titoli_accademici?.length > 0 && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>
                    <span className={styles.sectionIcon}>🎓</span>
                    Titoli accademici
                  </h2>
                  <ul className={styles.timeline}>
                    {medico.titoli_accademici.map((t, i) => (
                      <li key={i} className={styles.timelineItem}>
                        <span className={styles.timelineAnno}>{t.anno}</span>
                        <span className={styles.timelineTesto}>{t.titolo}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Esperienze Professionali */}
              {medico.esperienze_professionali?.length > 0 && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>
                    <span className={styles.sectionIcon}>💼</span>
                    Esperienze professionali
                  </h2>
                  <ul className={styles.timeline}>
                    {medico.esperienze_professionali.map((e, i) => (
                      <li key={i} className={styles.timelineItem}>
                        <span className={styles.timelineAnno}>{e.anno}</span>
                        <span className={styles.timelineTesto}>{e.descrizione}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Pubblicazioni */}
              {medico.pubblicazioni && (
                <div className={styles.section}>
                  <h2 className={styles.sectionTitle}>
                    <span className={styles.sectionIcon}>📄</span>
                    Pubblicazioni e ricerca
                  </h2>
                  <div className={styles.pubblicazioni}>
                    {medico.pubblicazioni.split("\n").filter(Boolean).map((riga, i) => (
                      <p key={i}>{riga}</p>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* SIDEBAR */}
            <aside className={styles.sidebar}>
              {medico.foto_url && (
                <div className={styles.fotoWrap}>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={medico.foto_url} alt={medico.nome_completo} className={styles.foto} />
                </div>
              )}

              <div className={styles.prenotaCard}>
                <p className={styles.prenotaLabel}>Vuoi prenotare una visita?</p>
                <a href={medico.link_prenota || "/cerca"} className={styles.prenotaBtn}>
                  PRENOTA UN ESAME O UNA VISITA
                </a>
              </div>

              <div className={styles.infoCard}>
                <div className={styles.infoRow}>
                  <span className={styles.infoIcon}>🏥</span>
                  <span>CDI – Centro Diagnostico Italiano</span>
                </div>
                <div className={styles.infoRow}>
                  <span className={styles.infoIcon}>📞</span>
                  <span>02 00 60 1</span>
                </div>
                <div className={styles.infoRow}>
                  <span className={styles.infoIcon}>🕐</span>
                  <span>Lun–Ven 7:00–20:00 · Sab 7:00–14:00</span>
                </div>
              </div>
            </aside>
          </div>
        </div>
      </div>

      {/* CTA BANNER */}
      <section className={styles.ctaBanner}>
        <div className={styles.container}>
          <p className={styles.ctaText}>Prenota una visita con {medico.nome_completo}</p>
          <a href={medico.link_prenota || "/cerca"} className={styles.ctaBannerBtn}>
            PRENOTA UN ESAME O UNA VISITA
          </a>
        </div>
      </section>
    </>
  );
}
