import { getMedici } from "@/lib/cms";
import styles from "./page.module.css";

export const revalidate = false;

export default async function MediciPage() {
  const medici = await getMedici() ?? [];

  // Raggruppa per specializzazione
  const gruppi = medici.reduce<Record<string, typeof medici>>((acc, m) => {
    const key = m.specializzazione || "Altro";
    if (!acc[key]) acc[key] = [];
    acc[key].push(m);
    return acc;
  }, {});

  const specializzazioni = Object.keys(gruppi).sort();

  return (
    <>
      <section className={styles.hero}>
        <div className={styles.heroBadge}>SPECIALISTI CDI</div>
        <h1 className={styles.heroTitle}>I Nostri Medici</h1>
        <p className={styles.heroSub}>
          Un team di specialisti qualificati al servizio della tua salute
        </p>
      </section>

      {/* Indice specializzazioni */}
      <nav className={styles.indice}>
        <div className={styles.container}>
          {specializzazioni.map((spec) => (
            <a key={spec} href={`#${slugify(spec)}`} className={styles.indiceLink}>
              {spec}
            </a>
          ))}
        </div>
      </nav>

      <div className={styles.container}>
        {specializzazioni.map((spec) => (
          <section key={spec} id={slugify(spec)} className={styles.gruppo}>
            <h2 className={styles.gruppoTitolo}>{spec}</h2>
            <div className={styles.grid}>
              {gruppi[spec].map((m) => (
                <a key={m.id} href={`/medici/${m.id}`} className={styles.card}>
                  {m.foto_url && (
                    /* eslint-disable-next-line @next/next/no-img-element */
                    <img src={m.foto_url} alt={m.nome_completo} className={styles.foto} />
                  )}
                  <div className={styles.cardBody}>
                    <p className={styles.nome}>{m.nome_completo}</p>
                    <p className={styles.ruolo}>{m.ruolo || m.specializzazione}</p>
                  </div>
                </a>
              ))}
            </div>
          </section>
        ))}

        {medici.length === 0 && (
          <p className={styles.empty}>Nessun medico disponibile al momento.</p>
        )}
      </div>
    </>
  );
}

function slugify(str: string) {
  return str.toLowerCase().replace(/\s+/g, "-").replace(/[^a-z0-9-]/g, "");
}
