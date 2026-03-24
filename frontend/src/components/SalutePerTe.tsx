"use client";
import { useState } from "react";
import styles from "./SalutePerTe.module.css";
import type { SalutePerTeArticolo } from "@/lib/cms";

const TABS = ["Consigli e approfondimenti", "News", "Comunicati stampa", "Articoli"];

export default function SalutePerTe({ articoli }: { articoli?: SalutePerTeArticolo[] | null }) {
  const [activeTab, setActiveTab] = useState(TABS[0]);
  const [page, setPage] = useState(0);

  const items = (articoli ?? []).filter((a) => a.tab === activeTab);
  const totalPages = Math.max(1, Math.ceil(items.length / 4));
  const visibili = items.slice(page * 4, page * 4 + 4);

  function handleTab(tab: string) {
    setActiveTab(tab);
    setPage(0);
  }

  return (
    <section className={styles.section}>
      <div className={styles.inner}>
        <h2 className={styles.title}>Salute per te</h2>

        <div className={styles.tabs}>
          {TABS.map((tab) => (
            <button
              key={tab}
              className={`${styles.tab} ${activeTab === tab ? styles.tabActive : ""}`}
              onClick={() => handleTab(tab)}
            >
              {tab}
            </button>
          ))}
        </div>

        <div className={styles.grid}>
          {visibili.map((a) => (
            <div key={a.id} className={styles.card}>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={a.immagine_url} alt={a.titolo} className={styles.cardImg} />
              <div className={styles.cardBody}>
                <h3 className={styles.cardTitle}>{a.titolo}</h3>
                <p className={styles.cardDesc}>{a.descrizione}</p>
                <a href={a.link} className={styles.cardLink}>Leggi ora</a>
              </div>
            </div>
          ))}
        </div>

        {totalPages > 1 && (
          <div className={styles.pagination}>
            <button className={styles.arrow} onClick={() => setPage((p) => Math.max(0, p - 1))}>←</button>
            <div className={styles.dots}>
              {Array.from({ length: totalPages }).map((_, i) => (
                <button key={i} className={`${styles.dot} ${i === page ? styles.dotActive : ""}`} onClick={() => setPage(i)} />
              ))}
            </div>
            <button className={styles.arrow} onClick={() => setPage((p) => Math.min(totalPages - 1, p + 1))}>→</button>
          </div>
        )}

        <div className={styles.ctaWrap}>
          <a href="#" className={styles.ctaBtn}>Scopri tutti →</a>
        </div>
      </div>
    </section>
  );
}
