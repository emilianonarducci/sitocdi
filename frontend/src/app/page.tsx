import SearchBar from "@/components/SearchBar";
import Hero from "@/components/Hero";
import ConsigliatiPerTe from "@/components/ConsigliatiPerTe";
import PercheSceglierci from "@/components/PercheSceglierci";
import SalutePerTe from "@/components/SalutePerTe";
import Newsletter from "@/components/Newsletter";
import AppDownload from "@/components/AppDownload";
import styles from "./page.module.css";

export default function HomePage() {
  return (
    <>
      {/* Hero full-width con carousel */}
      <Hero />

      {/* Consigliati per te */}
      <ConsigliatiPerTe />

      {/* Prenota una visita */}
      <SearchBar />

      {/* Servizi */}
      <section className={styles.services}>
        <div className="container">
          <div className={styles.sectionHeader}>
            <div>
              <h2 className={styles.sectionTitle}>Scopri i nostri servizi</h2>
              <p className={styles.sectionSubtitle}>
                Uno staff di oltre 2000 persone tra medici specialisti, tecnici sanitari, infermieri e impiegati
              </p>
            </div>
            <a href="#" className={styles.btnOutline}>Inizia da qui</a>
          </div>

          <div className={styles.filterTabs}>
            {["Le più visitate", "Donna", "Bambini", "Senior"].map((tab) => (
              <button key={tab} className={styles.filterTab}>{tab}</button>
            ))}
          </div>

          <div className={styles.servicesGrid}>
            {[
              {
                img: "https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=600&q=80&auto=format&fit=crop",
                title: "Visite specialistiche",
                desc: "Consulti con medici specialisti in tutte le principali branche della medicina.",
              },
              {
                img: "https://images.unsplash.com/photo-1516069677018-378515003435?w=600&q=80&auto=format&fit=crop",
                title: "Radiologia e Diagnostica",
                desc: "Tecnologie avanzate per diagnosi precise: RX, TC, RM, ecografie e molto altro.",
              },
              {
                img: "https://images.unsplash.com/photo-1551601651-2a8555f1a136?w=600&q=80&auto=format&fit=crop",
                title: "Chirurgia",
                desc: "Interventi chirurgici in day surgery con équipe specializzate e tecnologie all'avanguardia.",
              },
            ].map((s) => (
              <div key={s.title} className={styles.serviceCard}>
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={s.img} alt={s.title} className={styles.serviceImage} />
                <div className={styles.serviceBody}>
                  <h3>{s.title}</h3>
                  <p>{s.desc}</p>
                  <a href="#">Scopri di più →</a>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Perché sceglierci */}
      <PercheSceglierci />

      {/* Recensioni */}
      <section className={styles.reviews}>
        <div className="container">
          <div className={styles.sectionHeader}>
            <div>
              <h2 className={styles.sectionTitle}>Dicono di noi</h2>
              <p className={styles.sectionSubtitle}>Le esperienze dei nostri pazienti</p>
            </div>
          </div>
          <div className={styles.reviewsGrid}>
            {[
              { initials: "ML", name: "Maria L.", date: "15 febbraio 2026", stars: 5, text: "Personale molto professionale e gentile. Ho fatto una consulenza neurologica e sono rimasta molto soddisfatta." },
              { initials: "GP", name: "Giorgio P.", date: "3 marzo 2026", stars: 5, text: "Ho fatto un intervento neurochirurgico in day surgery. Equipe eccellente, tempi rispettati, recupero veloce." },
              { initials: "AR", name: "Anna R.", date: "10 marzo 2026", stars: 4, text: "Struttura moderna e pulita. Attese contenute e medici preparati. Lo consiglio a tutti." },
            ].map((r) => (
              <div key={r.name} className={styles.reviewCard}>
                <div className={styles.stars}>{"★".repeat(r.stars)}{"☆".repeat(5 - r.stars)}</div>
                <p className={styles.reviewText}>&quot;{r.text}&quot;</p>
                <div className={styles.author}>
                  <div className={styles.avatar}>{r.initials}</div>
                  <div>
                    <div className={styles.authorName}>{r.name}</div>
                    <div className={styles.authorDate}>{r.date}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
          <div className={styles.trustpilot}>
            <span className={styles.trustScore}>4.7</span>
            <span>★★★★★ su Trustpilot — oltre 2.400 recensioni verificate</span>
          </div>
        </div>
      </section>

      {/* Salute per te */}
      <SalutePerTe />

      {/* Newsletter */}
      <Newsletter />

      {/* App Download */}
      <AppDownload />
    </>
  );
}
