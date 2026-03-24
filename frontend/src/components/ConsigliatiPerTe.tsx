import styles from "./ConsigliatiPerTe.module.css";

const items = [
  {
    image: "https://www.cdi.it/wp-content/uploads/2024/12/2-Screening-gravidanza-cdi.jpg",
    title: "Prevenzione Uomo: Percorso Pausa in Salute Uomo",
    cta: "Scopri check up",
  },
  {
    image: "https://www.cdi.it/wp-content/uploads/2025/02/CDI_VECTRA_Banner-scaled.jpg",
    title: "Essere vegetariani: benefici e accortezze",
    cta: "Leggi ora",
  },
  {
    image: "https://www.cdi.it/wp-content/uploads/2026/01/Header_Runner_SitoCDI-1.png",
    title: "Invita un amico per ottenere uno sconto",
    cta: "Il tuo sconto subito",
  },
];

export default function ConsigliatiPerTe() {
  return (
    <section className={styles.section}>
      <div className="container">
        <h3 className={styles.title}>Consigliati per te</h3>
        <div className={styles.grid}>
          {items.map((item) => (
            <a href="#" key={item.title} className={styles.card}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={item.image} alt={item.title} className={styles.cardImage} />
              <div className={styles.cardBody}>
                <p className={styles.cardTitle}>{item.title}</p>
                <span className={styles.cardCta}>{item.cta}</span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
