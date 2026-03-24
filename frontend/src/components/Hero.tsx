"use client";
import { useState } from "react";
import styles from "./Hero.module.css";

const slides = [
  {
    badge: "Novità",
    title: "50 anni CDI",
    text: "Il 21 marzo 1975 il Centro Diagnostico Italiano apriva le porte ai suoi primi pazienti. Da quel giorno sono passati cinquant'anni.",
    cta: "Scopri di più",
    image: "https://www.cdi.it/wp-content/uploads/2025/05/CDI_Slider_Cinquantesimo-scaled.jpg",
  },
  {
    badge: "Diagnostica",
    title: "Tecnologie all'avanguardia",
    text: "RX, TC, RM, ecografie e molto altro. Strumenti digitali per diagnosi precise e veloci.",
    cta: "Scopri i servizi",
    image: "https://www.cdi.it/wp-content/uploads/2024/12/2-Screening-gravidanza-cdi.jpg",
  },
  {
    badge: "Prenotazione",
    title: "Prenota online",
    text: "Trova la prestazione, scegli il centro e la data. Semplice, veloce, vicino a te.",
    cta: "Prenota ora",
    image: "https://www.cdi.it/wp-content/uploads/2025/02/CDI_VECTRA_Banner-scaled.jpg",
  },
];

export default function Hero() {
  const [current, setCurrent] = useState(0);

  const prev = () => setCurrent((c) => (c === 0 ? slides.length - 1 : c - 1));
  const next = () => setCurrent((c) => (c === slides.length - 1 ? 0 : c + 1));

  const slide = slides[current];

  return (
    <section className={styles.hero}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img src={slide.image} alt="" className={styles.bgImage} />
      <div className={styles.overlay} />

      <div className={styles.content}>
        <span className={styles.badge}>{slide.badge}</span>
        <h1>{slide.title}</h1>
        <p>{slide.text}</p>
        <a href="#" className={styles.cta}>
          {slide.cta} →
        </a>
      </div>

      <div className={styles.nav}>
        <button className={styles.arrow} onClick={prev} aria-label="Precedente">←</button>
        <div className={styles.dots}>
          {slides.map((_, i) => (
            <button
              key={i}
              className={`${styles.dot} ${i === current ? styles.dotActive : ""}`}
              onClick={() => setCurrent(i)}
              aria-label={`Slide ${i + 1}`}
            />
          ))}
        </div>
        <button className={styles.arrow} onClick={next} aria-label="Successivo">→</button>
      </div>
    </section>
  );
}
