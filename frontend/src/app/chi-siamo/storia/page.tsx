import styles from "./page.module.css";

export const metadata = {
  title: "La Nostra Storia | CDI Centro Diagnostico Italiano",
  description: "Cinquant'anni insieme: la storia del Centro Diagnostico Italiano, dalla fondazione nel 1975 ad oggi.",
};

const TIMELINE = [
  { anno: "1975", titolo: "Fondazione", desc: "Inaugurazione della sede centrale di Via Saint Bon 20, Milano, il 21 marzo 1975. CDI apre con poliambulatorio, laboratorio analisi e reparto di radiologia, sull'idea innovativa di portare prevenzione e diagnosi precoce sul territorio." },
  { anno: "1976", titolo: "Convenzione SSN", desc: "Laboratorio analisi e radiologia vengono convenzionati con il Servizio Sanitario Nazionale, garantendo accesso alle cure e continuità assistenziale." },
  { anno: "1984", titolo: "Primo ambulatorio in centro città", desc: "Apertura del primo ambulatorio multidisciplinare nel centro di Milano, in Largo Cairoli. Avvio della computerizzazione dei processi di accettazione e refertazione." },
  { anno: "1989", titolo: "Imaging avanzato", desc: "Installazione delle prime apparecchiature TC (tomografia computerizzata) e RM (risonanza magnetica), per potenziare la diagnosi precoce delle malattie." },
  { anno: "1997", titolo: "Certificazione ISO 9002", desc: "CDI ottiene la certificazione ISO 9002, confermando il proprio impegno verso standard di qualità internazionali." },
  { anno: "2004", titolo: "CyberKnife", desc: "Installazione del primo sistema di radiochirurgia robotica CyberKnife in Italia, che consente trattamenti radioterapici robotizzati di altissima precisione per la cura dei tumori." },
  { anno: "2006", titolo: "Joint Commission International", desc: "CDI diventa il primo centro ambulatoriale in Italia a ottenere l'accreditamento Joint Commission International (JCI), il massimo riconoscimento internazionale per la qualità delle strutture sanitarie." },
  { anno: "2010", titolo: "Centro di Riabilitazione", desc: "Apertura del centro di fisioterapia e riabilitazione, dotato di piscine terapeutiche e percorsi personalizzati." },
  { anno: "2018", titolo: "JCI per tutte le strutture", desc: "L'accreditamento JCI viene esteso a tutti i policlinici e al centro di riabilitazione." },
  { anno: "2019", titolo: "CDI Dental & Face", desc: "Lancio della divisione CDI Dental & Face per la medicina dentale e la medicina estetica integrata." },
  { anno: "2021", titolo: "Espansione regionale", desc: "Inaugurazione della nuova clinica di Varese, apertura di CDI Bicocca e CDI Pellegrino Rossi, acquisizione del centro diagnostico per immagini SME." },
  { anno: "2024", titolo: "35ª struttura", desc: "Apertura di Bionics Symbiosis nella nuova area di sviluppo urbano di Milano, portando a 35 il numero totale di strutture sul territorio." },
  { anno: "2025", titolo: "50° Anniversario", desc: "Celebrazioni del 50° anniversario. Installazione della TC a conteggio di fotoni (Photon-counting CT) e introduzione della mappatura totale dei nevi con AI integrata." },
];

const STATS = [
  { valore: "1975", label: "Anno di fondazione" },
  { valore: "35", label: "Strutture sul territorio" },
  { valore: "2.000+", label: "Professionisti" },
  { valore: "20 mln", label: "Pazienti in 50 anni" },
  { valore: "165 mln", label: "Prestazioni in 50 anni" },
  { valore: "€150 mln", label: "Ricavi 2024" },
];

export default function NostráStoriaPage() {
  return (
    <>
      {/* HERO */}
      <section className={styles.hero}>
        <div className={styles.heroInner}>
          <p className={styles.heroBadge}>DAL 1975</p>
          <h1 className={styles.heroTitle}>La Nostra Storia</h1>
          <p className={styles.heroSub}>
            Cinquant&apos;anni insieme: vicini di salute, da cinquant&apos;anni.
          </p>
        </div>
      </section>

      {/* APERTURA */}
      <section className={styles.apertura}>
        <div className={styles.container}>
          <p className={styles.lead}>
            Il Centro Diagnostico Italiano nasce nel <strong>1975</strong> dall&apos;intuizione
            dell&apos;imprenditore Fulvio Bracco e del professor Sergio Chiappa, radiologo
            presso l&apos;Ospedale Fatebenefratelli di Milano. La loro visione fondativa puntava
            sulla <strong>prevenzione</strong>, sulla <strong>diagnosi precoce</strong> e sulla{" "}
            <strong>medicina di prossimità</strong> — principi che CDI mantiene dopo cinque decenni.
          </p>
        </div>
      </section>

      {/* STATISTICHE */}
      <section className={styles.statsSection}>
        <div className={styles.container}>
          <div className={styles.statsGrid}>
            {STATS.map((s) => (
              <div key={s.label} className={styles.statCard}>
                <span className={styles.statValore}>{s.valore}</span>
                <span className={styles.statLabel}>{s.label}</span>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* TIMELINE */}
      <section className={styles.timelineSection}>
        <div className={styles.container}>
          <h2 className={styles.sectionTitle}>Le tappe principali</h2>
          <div className={styles.timeline}>
            {TIMELINE.map((item, i) => (
              <div key={item.anno} className={`${styles.timelineItem} ${i % 2 === 0 ? styles.left : styles.right}`}>
                <div className={styles.timelineContent}>
                  <span className={styles.timelineAnno}>{item.anno}</span>
                  <h3 className={styles.timelineTitolo}>{item.titolo}</h3>
                  <p className={styles.timelineDesc}>{item.desc}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* QUOTE */}
      <section className={styles.quoteSection}>
        <div className={styles.container}>
          <blockquote className={styles.quote}>
            &ldquo;Non celebriamo solo una ricorrenza ma un&apos;idea di sanità che ci guida da mezzo
            secolo: un&apos;idea innovativa per quell&apos;epoca che ebbe subito un grande successo
            perché puntava sulla prevenzione, sulla diagnosi precoce e sulla medicina di prossimità.&rdquo;
          </blockquote>
          <p className={styles.quoteAuthor}>Dott.ssa Diana Bracco — Presidente e CEO</p>
        </div>
      </section>

      {/* LEADERSHIP */}
      <section className={styles.leadershipSection}>
        <div className={styles.container}>
          <h2 className={styles.sectionTitle}>Leadership</h2>
          <div className={styles.leaderGrid}>
            {[
              { nome: "Dott.ssa Diana Bracco", ruolo: "Presidente e CEO" },
              { nome: "Dott. Andrea Mecenero", ruolo: "Chief Executive Officer" },
              { nome: "Prof. Andrea Casasco", ruolo: "Direttore Sanitario" },
            ].map((l) => (
              <div key={l.nome} className={styles.leaderCard}>
                <p className={styles.leaderNome}>{l.nome}</p>
                <p className={styles.leaderRuolo}>{l.ruolo}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
