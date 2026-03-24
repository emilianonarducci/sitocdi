import styles from "./PercheSceglierci.module.css";

const cards = [
  {
    variant: "light",
    icon: (
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
        {/* Flask / beaker */}
        <path d="M12 4h8M13 4v8L7 22a3 3 0 0 0 2.5 4.5h13A3 3 0 0 0 25 22l-6-10V4" stroke="#003087" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
        <circle cx="12" cy="20" r="1.5" fill="#003087"/>
        <circle cx="17" cy="23" r="1" fill="#003087"/>
      </svg>
    ),
    title: "Innovazione",
    desc: "Il CDI investe costantemente in tecnologie diagnostiche avanzate, soluzioni digitali e ricerca clinica per garantire esami di qualità.",
  },
  {
    variant: "mid",
    icon: (
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
        {/* Stethoscope */}
        <path d="M10 6v8a6 6 0 0 0 12 0V6" stroke="white" strokeWidth="2" strokeLinecap="round"/>
        <path d="M10 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" stroke="white" strokeWidth="1.5"/>
        <path d="M22 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z" stroke="white" strokeWidth="1.5"/>
        <path d="M16 20v4a4 4 0 0 0 8 0v-2" stroke="white" strokeWidth="2" strokeLinecap="round"/>
        <circle cx="26" cy="22" r="2.5" stroke="white" strokeWidth="1.5"/>
        <path d="M25 22h2M26 21v2" stroke="white" strokeWidth="1.2" strokeLinecap="round"/>
      </svg>
    ),
    title: "+80 Centri in Lombardia",
    desc: "Siamo presenti sul territorio lombardo con 35 sedi, di cui 22 poliambulatori.",
  },
  {
    variant: "dark",
    icon: (
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
        {/* Heart with hands */}
        <path d="M16 12c0-3.3-2.7-6-6-6a6 6 0 0 0-6 6c0 7 12 14 12 14s12-7 12-14a6 6 0 0 0-6-6c-3.3 0-6 2.7-6 6z" stroke="white" strokeWidth="2" strokeLinejoin="round"/>
        <path d="M8 28c0-2 1.5-3 4-3h8c2.5 0 4 1 4 3" stroke="white" strokeWidth="2" strokeLinecap="round"/>
      </svg>
    ),
    title: "Eccellenza clinica",
    desc: "Fare della ricerca costante dell'eccellenza clinica e dello sviluppo tecnologico il carattere distintivo di CDI.",
  },
];

export default function PercheSceglierci() {
  return (
    <section className={styles.section}>
      {/* Immagine di sfondo */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src="https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=1600&q=80&auto=format&fit=crop"
        alt=""
        className={styles.bgImg}
      />
      {/* Overlay gradiente */}
      <div className={styles.overlay} />

      {/* Contenuto */}
      <div className={styles.inner}>
        {/* Testo in alto a sinistra */}
        <div className={styles.textBlock}>
          <h2>Perché sceglierci</h2>
          <p>
            Ascoltare e comprenderne le esigenze, ricercare con continuità la
            personalizzazione del &quot;servizio&quot; e offrire la migliore soluzione
            per soddisfarne le aspettative.
          </p>
        </div>

        {/* Cards in basso */}
        <div className={styles.cards}>
          {cards.map((c) => (
            <div key={c.title} className={`${styles.card} ${styles[`card_${c.variant}`]}`}>
              <div className={styles.iconWrap}>{c.icon}</div>
              <h3>{c.title}</h3>
              <p>{c.desc}</p>
            </div>
          ))}
        </div>
      </div>

      {/* Frecce */}
      <button className={`${styles.arrow} ${styles.arrowLeft}`}>←</button>
      <button className={`${styles.arrow} ${styles.arrowRight}`}>→</button>
    </section>
  );
}
