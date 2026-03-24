"use client";
import { useState } from "react";
import styles from "./SalutePerTe.module.css";

const tabs = ["Consigli e approfondimenti", "News", "Comunicati stampa", "Articoli"];

const articles = {
  "Consigli e approfondimenti": [
    {
      img: "https://images.unsplash.com/photo-1501700493788-fa1a4fc9fe62?w=400&q=80&auto=format&fit=crop",
      title: "Benessere in viaggio: tutti i consigli",
      desc: "Dalle mete ideali agli accorgimenti per la tua salute.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=400&q=80&auto=format&fit=crop",
      title: "CDI per le donne",
      desc: "Percorsi di prevenzione, diagnosi e cura pensati per la salute femminile.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=400&q=80&auto=format&fit=crop",
      title: "È arrivata la tariffa YOUNG",
      desc: "Per i pazienti di età compresa tra i 18 e i 30 anni.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400&q=80&auto=format&fit=crop",
      title: "Come avvicinare i bambini agli sport invernali",
      desc: "Alcuni consigli da seguire affinché i nostri figli possano divertirsi.",
      link: "#",
    },
  ],
  "News": [
    {
      img: "https://images.unsplash.com/photo-1504813184591-01572f98c85f?w=400&q=80&auto=format&fit=crop",
      title: "CDI amplia i servizi di cardiologia",
      desc: "Nuovi macchinari di ultima generazione disponibili nelle sedi di Milano.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400&q=80&auto=format&fit=crop",
      title: "Nuova sede a Bergamo",
      desc: "Apriamo un nuovo poliambulatorio nel cuore di Bergamo.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=400&q=80&auto=format&fit=crop",
      title: "CDI e la ricerca oncologica",
      desc: "Il nostro impegno nella diagnosi precoce dei tumori.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1532938911079-1b06ac7ceec7?w=400&q=80&auto=format&fit=crop",
      title: "Accordo con i principali fondi sanitari",
      desc: "Ampliata la copertura per FASI, Metasalute e Unisalute.",
      link: "#",
    },
  ],
  "Comunicati stampa": [
    {
      img: "https://images.unsplash.com/photo-1568667256549-094345857637?w=400&q=80&auto=format&fit=crop",
      title: "CDI ottiene la certificazione ISO 9001",
      desc: "Ulteriore riconoscimento della qualità dei nostri servizi sanitari.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=400&q=80&auto=format&fit=crop",
      title: "Partnership con l'Università di Milano",
      desc: "Firmato accordo per la ricerca e la formazione medica.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1461897104016-0b3b00cc81ee?w=400&q=80&auto=format&fit=crop",
      title: "Bilancio di sostenibilità 2025",
      desc: "Il nostro impegno verso l'ambiente e la comunità.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1587370560942-ad2a04eabb6d?w=400&q=80&auto=format&fit=crop",
      title: "Nuovo piano strategico 2026-2028",
      desc: "Presentato il piano di sviluppo per i prossimi tre anni.",
      link: "#",
    },
  ],
  "Articoli": [
    {
      img: "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=400&q=80&auto=format&fit=crop",
      title: "Alimentazione e prevenzione",
      desc: "Come una dieta equilibrata riduce il rischio di malattie croniche.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1571019614242-c5c5dee9f50b?w=400&q=80&auto=format&fit=crop",
      title: "Attività fisica dopo i 50 anni",
      desc: "Consigli pratici per mantenersi in forma in ogni fase della vita.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=400&q=80&auto=format&fit=crop",
      title: "Il sonno e la salute mentale",
      desc: "L'importanza di dormire bene per il benessere psicofisico.",
      link: "#",
    },
    {
      img: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=400&q=80&auto=format&fit=crop",
      title: "Vaccini e prevenzione",
      desc: "Tutto quello che devi sapere sulle vaccinazioni raccomandate.",
      link: "#",
    },
  ],
};

export default function SalutePerTe() {
  const [activeTab, setActiveTab] = useState(tabs[0]);
  const [page, setPage] = useState(0);

  const items = articles[activeTab as keyof typeof articles] ?? [];
  const totalPages = 5; // mock

  function handleTab(tab: string) {
    setActiveTab(tab);
    setPage(0);
  }

  return (
    <section className={styles.section}>
      <div className={styles.inner}>
        <h2 className={styles.title}>Salute per te</h2>

        {/* Tabs */}
        <div className={styles.tabs}>
          {tabs.map((tab) => (
            <button
              key={tab}
              className={`${styles.tab} ${activeTab === tab ? styles.tabActive : ""}`}
              onClick={() => handleTab(tab)}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Cards */}
        <div className={styles.grid}>
          {items.map((article) => (
            <div key={article.title} className={styles.card}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={article.img} alt={article.title} className={styles.cardImg} />
              <div className={styles.cardBody}>
                <h3 className={styles.cardTitle}>{article.title}</h3>
                <p className={styles.cardDesc}>{article.desc}</p>
                <a href={article.link} className={styles.cardLink}>Leggi ora</a>
              </div>
            </div>
          ))}
        </div>

        {/* Pagination */}
        <div className={styles.pagination}>
          <button
            className={styles.arrow}
            onClick={() => setPage((p) => Math.max(0, p - 1))}
          >
            ←
          </button>
          <div className={styles.dots}>
            {Array.from({ length: totalPages }).map((_, i) => (
              <button
                key={i}
                className={`${styles.dot} ${i === page ? styles.dotActive : ""}`}
                onClick={() => setPage(i)}
              />
            ))}
          </div>
          <button
            className={styles.arrow}
            onClick={() => setPage((p) => Math.min(totalPages - 1, p + 1))}
          >
            →
          </button>
        </div>

        {/* CTA */}
        <div className={styles.ctaWrap}>
          <a href="#" className={styles.ctaBtn}>Scopri tutti →</a>
        </div>
      </div>
    </section>
  );
}
