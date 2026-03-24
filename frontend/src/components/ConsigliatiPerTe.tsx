import styles from "./ConsigliatiPerTe.module.css";
import type { ConsigliatiCard } from "@/lib/cms";

const FALLBACK: ConsigliatiCard[] = [
  { id: 1, titolo: "Visita cardiologica", immagine_url: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=300&q=80&auto=format&fit=crop", link: "/cerca?q=visita+cardiologica" },
  { id: 2, titolo: "Esami del sangue", immagine_url: "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=300&q=80&auto=format&fit=crop", link: "/cerca?q=esame+sangue" },
  { id: 3, titolo: "Ecografia", immagine_url: "https://images.unsplash.com/photo-1576671081837-49000212a370?w=300&q=80&auto=format&fit=crop", link: "/cerca?q=ecografia" },
];

export default function ConsigliatiPerTe({ cards: initialCards }: { cards?: ConsigliatiCard[] | null }) {
  const items = initialCards?.length ? initialCards : FALLBACK;
  return (
    <section className={styles.section}>
      <div className="container">
        <h3 className={styles.title}>Consigliati per te</h3>
        <div className={styles.grid}>
          {items.map((item) => (
            <a href={item.link} key={item.id} className={styles.card}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={item.immagine_url} alt={item.titolo} className={styles.cardImage} />
              <div className={styles.cardBody}>
                <p className={styles.cardTitle}>{item.titolo}</p>
                <span className={styles.cardCta}>Scopri di più</span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
